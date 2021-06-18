import time,mysql.connector,smtplib
from datetime import datetime
from time import strftime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from commandes import database,planning
class scan:
    def __init__(self):
        self.path = 'waiting_list.txt'
        fichier = open(self.path,"r")
        liste_init = []
        for ligne in fichier:
            liste_init.append(ligne)
        self.timer = 3600
        self.database = mysql.connector.connect(
            host="localhost",
            user="hugodemenez",
            password="password",
            database="database",
            auth_plugin='mysql_native_password',
        )
        self.scruter(liste_init)
        
    def scruter(self,liste):
        cst =0
        user_data={}
        while True:
            if (datetime.now().strftime("%w")=="0") & (cst ==0): #si on est dimanche on envoie le planning,
                Liste = self.database.cursor()
                Liste.execute("SELECT * FROM user")
                for (username,password,email) in Liste:
                    planning().envoie_planning(username,password,email)                                   #on utilise une constante pour n'envoyer le mail qu'une fois
                cst=1
            if (datetime.now().strftime("%w")=="1"): 
                cst = 0

            new_liste = []
            fichier = open(self.path,"r")
            for ligne in fichier:
                new_liste.append(ligne)

            #Si les listes sont differentes alors quelqu'un s'est inscrit, on actualise la base de données
            if (new_liste != liste):
                Liste = self.database.cursor()
                Liste.execute("SELECT * FROM user")

                for (username,password,email) in Liste:
                    try:
                        data = database().complete_database(username,password)
                        #Regarde si le planning a changé
                        try:
                            if user_data[username]['planning']!=data['planning']:
                                self.notification_planning(email)
                                user_data[username]['planning']=data['planning']
                            #Regarde si les notes ont changé
                            if user_data[username]['marks']!=data['marks']:
                                self.notification_marks(email)
                                user_data[username]['marks']=data['marks']
                        except:
                            user_data[username]=data
                    except:
                        print("error with %s %s"%(username,email))
                    liste = new_liste
            fichier.close()

            #On complete la base de données toutes les 12heures même si personne s'est inscrit
            if self.timer >3600:
                Liste = self.database.cursor()
                Liste.execute("SELECT * FROM user")
                for (username,password,email) in Liste:
                    try:
                        data = database().complete_database(username,password)
                        #Regarde si le planning a changé
                        try:
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
                        except:
                            user_data[username]=data
                            self.notification_data(email)
                    except:
                        print("error with %s %s"%(username,email))
                self.timer=0

            time.sleep(1)
            self.timer +=1

    def notification_marks(self,email,liste):
        msg = MIMEMultipart()
        msg['From'] = 'ProjetInfoIsen2021@gmail.com' #adresse mail de départ, ici celle du projet
        msg['To'] = email #destinataire
        msg['Subject'] = "ISENINFO - Notification" #objet du mail
        #Message du mail
        text =""
        for event in liste:
            text+= str(event['title'])+' : '+str(event['mark'])+' le '+str(event['date'])+'<br>'
        html_txt =f"""
        <body>
            <h1>Bonjour</h1>
            <p>Vous avez une nouvelle note : <br>{text} </p>
            <a href="http://www.iseninfo.fr">Se connecter</a>
            <br>
            <br>
            <img src="https://raw.githubusercontent.com/hugodemenez/Projet_2021_Informatique/a5813057a8d3f4d0fdbab5b2b5b5413bb8ce7322/assets/undraw_instat_analysis_ajld.svg" width=50%>
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
        for event in liste:
            text+= str(event['cours'])+' avec '+str(event['professeur'])+' en '+str(event['salle'])+' le '+str(event['date_debut'])+' de '+str(event['heure_debut'])+' à '+str(event['heure_fin'])+'<br>'
        html_txt =f"""
        <body>
            <h1>Bonjour</h1>
            <p>Vous avez une changement dans votre planning : <br>{text} </p>
            <a href="http://www.iseninfo.fr">Se connecter</a>
            <br>
            <br>
            <img src="https://raw.githubusercontent.com/hugodemenez/Projet_2021_Informatique/bd2d26a1c5dff6168de02c8b2067e86a0872c3aa/assets/undraw_schedule_pnbk.svg" width=50%>
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
        <img src="https://raw.githubusercontent.com/hugodemenez/Projet_2021_Informatique/bd2d26a1c5dff6168de02c8b2067e86a0872c3aa/assets/undraw_data_reports_706v.svg" width=50%>
        </body>"""
        
        msg.attach(MIMEText(html_txt,'html'))
        mailserver = smtplib.SMTP('smtp.gmail.com', 587)    #serveur et numéro du port pour envoyer le mail
        mailserver.ehlo()
        mailserver.starttls()
        mailserver.ehlo()
        mailserver.login('ProjetInfoIsen2021@gmail.com', 'gloubiboulga1') #on se connecte au compte gmail pour envoyer le mail
        mailserver.sendmail('ProjetInfoIsen2021@gmail.com', email, msg.as_string()) #on envoie le mail
        mailserver.quit()
        print("Notification base de donnée envoyée à %s"%email)
            


if __name__ == "__main__":
    scan()