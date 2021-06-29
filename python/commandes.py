from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import smtplib
from datetime import datetime
from webscraping import scraping
from google_auth_oauthlib.flow import Flow, InstalledAppFlow
from googleapiclient.discovery import build
import mysql.connector,time

class planning:
    def __init__(self):
        pass
   
    def envoie_planning(self,username,password,email):
        """
        Cette fonction sert à envoyer le planning (recupéré avec le webscraping) par mail avec un formattage texte/html et de joindre un fichier .csv pour 
        pouvoir ajouter ce dernier dans le calendrier GoogleAgenda en quelques clics
        """
        try:
            planning_text =''
            planning =scraping().get_planning(username = username,password = password)
            self.initialiser_csv('planning.csv')
            for i in planning:
                self.ajouter(i['cours'],i['date_debut'],i['heure_debut'],i['date_fin'],i['heure_fin'],i['professeur'],i['salle'],'planning.csv')
                planning_text+=i['cours'] +' avec '+str(i['professeur'])+' en salle '+str(i['salle'])+' le '+str(i['date_debut'])+' de '+str(i['heure_debut'])+' à '+str(i['heure_fin'])+"<br>"
            self.envoyer_planning_email(destinataire=email,text=planning_text)
            return planning
        except Exception as error:
            print(error)
            return

    def initialiser_csv(self,chemin):
        """
        Cette fonction sert à initialiser le fichier csv pour pouvoir y ajouter des elements par la suite
        """
        fichier = open(chemin,"w")
        fichier.write("subject,Start Date,Start Time, End Date, End Time, Description,Location\n")
        fichier.close()

    def ajouter(self,cours,date_debut, heure_debut,date_fin,heure_fin,professeur,salle,chemin):
        """
        Cette fonction sert à ajouter des evenements dans le fichiers .csv
        """
        fichier = open(chemin,"a")
        fichier.write("%s,%s,%s,%s,%s,%s,%s"%(cours,date_debut,heure_debut,date_fin,heure_fin,professeur,salle))
        fichier.write("\n")
        fichier.close()

    def envoyer_planning_email(self,destinataire,text):
        """
        Cette fonction sert à envoyer le planning par mail en joignant le fichier .csv
        """

        #On intialise le message avec la classe MIMEMultipart
        msg = MIMEMultipart()
        msg['From'] = 'ProjetInfoIsen2021@gmail.com' #adresse mail de départ, ici celle du projet
        msg['To'] = destinataire #destinataire
        msg['Subject'] = 'Emploi du temps semaine du ' + str(datetime.now().day) + '-' + str(datetime.now().month) + '-' + str(datetime.now().year) #objet du mail
        
        #On formate le contenu du mail
        html_txt = f"""
        <body>
            <h1>Bonjour</h1>
            <p>Veuillez trouver votre planning ci-dessous :</p>
            <p>{text}</p>
            <a href="http://www.iseninfo.fr">Se connecter</a>
            <br>
            <br>
            <img src="https://raw.githubusercontent.com/hugodemenez/Projet_2021_Informatique/bd2d26a1c5dff6168de02c8b2067e86a0872c3aa/assets/undraw_schedule_pnbk.svg" width=100%>
        </body>
        """

        nom_fichier = "planning.csv"    ## Spécification du nom de la pièce jointe
        piece = open("planning.csv", "rb")    ## Ouverture du fichier
        part = MIMEBase('application', 'octet-stream')    ## Encodage de la pièce jointe en Base64
        part.set_payload((piece).read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', "piece; filename= %s" % nom_fichier)
        msg.attach(part)    ## Attache de la pièce jointe à l'objet "message" 
        
        msg.attach(MIMEText(html_txt,'html'))
        mailserver = smtplib.SMTP('smtp.gmail.com', 587)    #serveur et numéro du port pour envoyer le mail
        mailserver.ehlo()
        mailserver.starttls()
        mailserver.ehlo()
        mailserver.login('ProjetInfoIsen2021@gmail.com', 'gloubiboulga1') #on se connecte au compte gmail pour envoyer le mail
        mailserver.sendmail('ProjetInfoIsen2021@gmail.com', destinataire, msg.as_string()) #on envoie le mail
        mailserver.quit()




class database:
    #On initalise la classe en créant une variable de connexion à la base de données ainsi que l'initialisation du curseur pour effectuer les requetes
    def __init__(self):
        self.database = mysql.connector.connect(
        host="localhost",
        user="hugodemenez",
        password="password",
        database="database",
        auth_plugin='mysql_native_password',
        )
        self.cursor = self.database.cursor()


    def complete_database(self,username,password):
        """
        Cette fonction sert à completer la base de données avec le planning et les notes pour l'utilisateur renseigné avec son nom et son mot de passe qui sont passés en arguments
        de la fonction
        """
        try:
            #On effectue le webscraping du planning pour le stocker dans une variable
            planning = scraping().get_planning(username,password)
            #On ajoute les élements du planning dans la base de données en associant le nom d'utilisateur correspondant
            self.add_planning_to_database(planning,username)
            #On effectue le webscraping des notes pour les stocker dans une variable
            marks = scraping().get_marks(username,password)
            #On ajoute les differentes notes dans la base de données en associant le nom d'utilisateur correspondant
            self.add_marks_to_database(marks,username)
            #On renvoit les differents dictionnaires (planning et notes) dans un autre dictionnaire pour pouvoir réutiliser les informations par la suite
            return {'planning':planning,'marks':marks}
        except Exception as error:
            raise Exception(error)

    def add_planning_to_database(self,planning:dict,username:str):
        """
        Cette fonction sert à ajouter les elements du planning dans la base de données
        """
        try:
            #On initialise la variable number pour avoir un identifiant différent pour chaque evenement
            number = 0
            #On initialise la requete pour supprimer le planning déjà existant pour l'utilisateur
            sql = "DELETE FROM planning WHERE username= '%s'" % (username)
            #On execute la requete
            self.cursor.execute(sql)
            #On applique les changements
            self.database.commit()
            #Pour tous les evenements, on formate de la même maniere en incrémentant la variable number pour etre sûr d'avoir un id different pour chaque cours
            for cours in planning:
                id = number
                room = cours['salle']
                teacher = cours['professeur']
                date = cours['date_debut']
                start = cours['heure_debut']
                end = cours['heure_fin']
                subject = cours['cours']
                sql="INSERT INTO planning (id,room, teacher,date,start,end,subject,username) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
                self.cursor.execute(sql,(str(id)+username,room,teacher,date,start,end,subject,username))
                self.database.commit()
                number +=1
        except Exception as error:
            print(error)
        
    def add_marks_to_database(self,marks:dict,username:str):
        """
        Cette fonction sert à ajouter les différentes notes dans la base de données
        """
        try:
            #On initialise la variable number pour avoir un identifiant différent pour chaque note
            number = 0
            #On initialise la requete pour supprimer les notes déjà existantes pour l'utilisateur
            sql = "DELETE FROM marks WHERE username= '%s'" % (username)
            #On execute la requete
            self.cursor.execute(sql)
            self.database.commit()
            #Pour toutes les notes, on formate de la même maniere en incrémentant la variable number pour etre sûr d'avoir un id different pour chaque note
            for mark in marks:
                id = str(number)
                title = mark['title']
                __mark = mark['mark']
                date = mark['date']
                sql="INSERT INTO marks (id,title,mark,date,username) VALUES (%s,%s,%s,%s,%s)"
                self.cursor.execute(sql,(id+username,title,__mark,date,username))
                self.database.commit()
                number +=1
        except Exception as error:
            print(error)





if __name__ == "__main__":
    pass
