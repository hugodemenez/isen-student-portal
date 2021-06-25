import time,mysql.connector,smtplib
from datetime import datetime
from time import strftime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from commandes import database,planning


#On definit une classe qui permet de lancer la fonction de scrutage des données
class scan:
    def __init__(self):
        self.timer = 0
        self.scruter()
        
    def scruter(self):
        cst =0
        user_data={}
        #On se connecte à la base de données
        self.database = mysql.connector.connect(host="localhost",user="hugodemenez",password="password",database="database",auth_plugin='mysql_native_password')
        Liste = self.database.cursor()
        #On regarde tous les utilisateurs inscrits dans la base de données avant de rentrer dans la boucle while afin de ne pas avertir les utilisateurs déjà existants
        Liste.execute("SELECT * FROM user")
        for (username,password,email) in Liste:
            #On affiche dans la console l'identifiant de l'utilisateur pour lequel on charge les données
            print("Chargement des données pour %s"%username)
            try:
                data = database().complete_database(username,password)
                #On ajoute les données dans le dictionnaire des utilisateurs déjà inscrits
                user_data[username]=data
            #S'il y a une erreur alors cela implique que les données de l'utilisateur ne sont pas les mêmes sur Aurion (impossible de se connecter) on le retire de la base de données
            #Et il faut lui envoyer un mail pour l'avertir
            except:
                connection = mysql.connector.connect(host="localhost",user="hugodemenez",password="password",database="database",auth_plugin='mysql_native_password')
                cursor = connection.cursor(buffered=True)
                #On initialise la requete pour supprimer les données de l'utilisateur
                sql = "DELETE FROM user WHERE username= '%s'" % (username)
                #On execute la requete
                cursor.execute(sql)
                #On applique les changements
                connection.commit()
                cursor.close()
                connection.close()
                self.notification_error(email,username,password)
        Liste.close()

        while True:
            #On actualise la connexion
            self.database = mysql.connector.connect(
            host="localhost",
            user="hugodemenez",
            password="password",
            database="database",
            auth_plugin='mysql_native_password',)
            if (datetime.now().strftime("%w")=="0") & (cst ==0): #si on est dimanche on envoie le planning,
                Liste = self.database.cursor()
                Liste.execute("SELECT * FROM user")
                for (username,password,email) in Liste:
                    planning().envoie_planning(username,password,email)
                Liste.close()
                #on utilise une constante pour n'envoyer le mail qu'une fois                                   
                cst=1
                
            #Si on change de jours alors on peut remettre cette constante à 0
            if (datetime.now().strftime("%w")=="1"): 
                cst = 0


            
            Liste = self.database.cursor()
            #On regarde tous les utilisateurs inscrits dans la base de données
            Liste.execute("SELECT * FROM user")
            for (username,password,email) in Liste:
                try:
                    #On regarde si on scrute déjà le planning et les notes pour l'utilisateur actuellement selectionné dans la boucle for
                    if username not in user_data:
                        #On affiche dans la console l'identifiant de l'utilisateur pour lequel on charge les données
                        print("Chargement des données pour %s"%username)
                        #On rafrachit la base de données
                        try:
                            data = database().complete_database(username,password)
                            #S'il vient de s'inscrire alors on arrive à ce stade et on peut ainsi le prevenir par mail
                            user_data[username]=data
                            self.notification_data(email)
                        
                        #Si il y a une exception cela implique que l'utilisateur n'existe pas, on le retire de la base de données et on lui envoie une notification
                        except:
                            connection = mysql.connector.connect(host="localhost",user="hugodemenez",password="password",database="database",auth_plugin='mysql_native_password')
                            cursor = connection.cursor(buffered=True)
                            #On initialise la requete pour supprimer les données de l'utilisateur
                            sql = "DELETE FROM user WHERE username= '%s'" % (username)
                            #On execute la requete
                            cursor.execute(sql)
                            #On applique les changements
                            connection.commit()
                            cursor.close()
                            connection.close()
                            self.notification_error(email,username,password)
                            #On lève l'exception pour pouvoir sortir de la boucle try
                            raise Exception("Il y a eu une erreur dans les identifiants Aurion")

                        #On lève l'exception pour pouvoir sortir de la boucle try
                        raise Exception("Les données ont été ajoutées dans la base de données")
                    
                    #On complete la base de données toutes les heures même si personne s'est inscrit
                    if self.timer == 3600:
                        #On rafrachit la base de données
                        data = database().complete_database(username,password)
                        #Si on arrive jusqu'ici cela signifie que l'utilisateur est déjà scruté, alors on regarde si son planning a changé
                        if user_data[username]['planning']!=data['planning']:
                            list_difference = []
                            for item in data['planning']:
                                if item not in user_data[username]['planning']:
                                    list_difference.append(item)
                            self.notification_planning(email,list_difference)
                            user_data[username]['planning']=data['planning']

                        #Regarde si les notes ont changé
                        if user_data[username]['marks']!=data['marks']:
                            list_difference = []
                            for item in data['marks']:
                                if item not in user_data[username]['marks']:
                                    list_difference.append(item)
                            self.notification_marks(email,list_difference)
                            user_data[username]['marks']=data['marks']

                        #On remet le timer à 0
                        self.timer=0

                #S'il y a une exception qui est levée alors on l'affiche dans la console en regardant pour quel utilisateur, celle ci est apparue
                except Exception as error:
                    print("Exception %s %s : %s"%(username,email,error))

            Liste.close()
            
            

            time.sleep(1)
            self.timer +=1

    def notification_marks(self,email,liste):
        msg = MIMEMultipart()
        msg['From'] = 'ProjetInfoIsen2021@gmail.com' #adresse mail de départ, ici celle du projet
        msg['To'] = email #destinataire
        msg['Subject'] = "ISENINFO - Notification" #objet du mail
        #Message du mail
        text =""
        #On créé le text sous forme de string afin de l'inclure dans le mail (il contient toutes les nouvelles notes mises en forme)
        for event in liste:
            text+= str(event['title'])+' : '+str(event['mark'])+' le '+str(event['date'])+'<br>'
        html_txt =f"""
        <body>
            <h1>Bonjour</h1>
            <p>Vous avez une nouvelle note : <br>{text} </p>
            <a href="http://www.iseninfo.fr">Se connecter</a>
            <br>
            <br>
            <img src="https://raw.githubusercontent.com/hugodemenez/Projet_2021_Informatique/a5813057a8d3f4d0fdbab5b2b5b5413bb8ce7322/assets/undraw_instat_analysis_ajld.svg" width=100%>
        </body>
        """

        msg.attach(MIMEText(html_txt,'html'))
        mailserver = smtplib.SMTP('smtp.gmail.com', 587)    #serveur et numéro du port pour envoyer le mail
        mailserver.ehlo()
        mailserver.starttls()
        mailserver.ehlo()
        mailserver.login('ProjetInfoIsen2021@gmail.com', 'gloubiboulga1') #on se connecte au compte gmail pour envoyer le mail
        mailserver.sendmail('ProjetInfoIsen2021@gmail.com', email, msg.as_string()) #on envoie le mail
        mailserver.quit()
        print("Notification note envoyée à %s"%email)

    def notification_planning(self,email,liste):
        msg = MIMEMultipart()
        msg['From'] = 'ProjetInfoIsen2021@gmail.com' #adresse mail de départ, ici celle du projet
        msg['To'] = email #destinataire
        msg['Subject'] = "ISENINFO - Notification" #objet du mail
        #Message du mail
        text =""
        #On créé le text sous forme de string afin de l'inclure dans le mail (il contient tous les nouveaux cours mis en forme)
        for event in liste:
            text+= str(event['cours'])+' avec '+str(event['professeur'])+' en '+str(event['salle'])+' le '+str(event['date_debut'])+' de '+str(event['heure_debut'])+' à '+str(event['heure_fin'])+'<br>'
        html_txt =f"""
        <body>
            <h1>Bonjour</h1>
            <p>Vous avez une changement dans votre planning : <br>{text} </p>
            <a href="http://www.iseninfo.fr">Se connecter</a>
            <br>
            <br>
            <img src="https://raw.githubusercontent.com/hugodemenez/Projet_2021_Informatique/bd2d26a1c5dff6168de02c8b2067e86a0872c3aa/assets/undraw_schedule_pnbk.svg" width=100%>
        </body>
        """
        msg.attach(MIMEText(html_txt,'html'))
        mailserver = smtplib.SMTP('smtp.gmail.com', 587)    #serveur et numéro du port pour envoyer le mail
        mailserver.ehlo()
        mailserver.starttls()
        mailserver.ehlo()
        mailserver.login('ProjetInfoIsen2021@gmail.com', 'gloubiboulga1') #on se connecte au compte gmail pour envoyer le mail
        mailserver.sendmail('ProjetInfoIsen2021@gmail.com', email, msg.as_string()) #on envoie le mail
        mailserver.quit()
        print("Notification planning envoyée à %s"%email)

    def notification_data(self,email):
        msg = MIMEMultipart()
        msg['From'] = 'ProjetInfoIsen2021@gmail.com' #adresse mail de départ, ici celle du projet
        msg['To'] = email #destinataire
        msg['Subject'] = "ISENINFO - Notification" #objet du mail
        #Message du mail
        html_txt = """<body>
        <h1>Bonjour</h1>
        <p>Vous pouvez dès à présent consulter vos notes et votre planning sur notre site</p>
        <a href="http://www.iseninfo.fr">Se connecter</a>
        <br>
        <br>
        <img src="https://raw.githubusercontent.com/hugodemenez/Projet_2021_Informatique/bd2d26a1c5dff6168de02c8b2067e86a0872c3aa/assets/undraw_data_reports_706v.svg" width=100%>
        </body>"""
        
        msg.attach(MIMEText(html_txt,'html'))
        mailserver = smtplib.SMTP('smtp.gmail.com', 587)    #serveur et numéro du port pour envoyer le mail
        mailserver.ehlo()
        mailserver.starttls()
        mailserver.ehlo()
        mailserver.login('ProjetInfoIsen2021@gmail.com', 'gloubiboulga1') #on se connecte au compte gmail pour envoyer le mail
        mailserver.sendmail('ProjetInfoIsen2021@gmail.com', email, msg.as_string()) #on envoie le mail
        mailserver.quit()
        print("Notification base de données envoyée à %s"%email)
            
    def notification_error(self,email,username,password):
        msg = MIMEMultipart()
        msg['From'] = 'ProjetInfoIsen2021@gmail.com' #adresse mail de départ, ici celle du projet
        msg['To'] = email #destinataire
        msg['Subject'] = "ISENINFO - Notification" #objet du mail
        #Message du mail
        html_txt = f"""<body>
        <h1>Bonjour</h1>
        <p>Il y a une erreur dans votre identifiant ou votre mot de passe Aurion :<br>
        - identifiant : {username}<br>
        - mot de passe : {password}<br>
        Veuillez réessayer votre inscription en <a href="http://www.iseninfo.fr">cliquant-ici</a></p>
        <br>
        <br>
        <img src="https://raw.githubusercontent.com/hugodemenez/Projet_2021_Informatique/eb9533477e2db9529bd264c8fe6e8b7d734cbcaa/assets/undraw_cancel_u1it.svg" width=100%>
        </body>"""
        
        msg.attach(MIMEText(html_txt,'html'))
        mailserver = smtplib.SMTP('smtp.gmail.com', 587)    #serveur et numéro du port pour envoyer le mail
        mailserver.ehlo()
        mailserver.starttls()
        mailserver.ehlo()
        mailserver.login('ProjetInfoIsen2021@gmail.com', 'gloubiboulga1') #on se connecte au compte gmail pour envoyer le mail
        mailserver.sendmail('ProjetInfoIsen2021@gmail.com', email, msg.as_string()) #on envoie le mail
        mailserver.quit()
        print("Notification erreur de connexion envoyée à %s"%email)
         

if __name__ == "__main__":
    scan()