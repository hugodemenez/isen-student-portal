from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import smtplib
from datetime import datetime
from webscraping import scraping
from google_auth_oauthlib.flow import Flow, InstalledAppFlow
from googleapiclient.discovery import build
import sqlite3
import mysql.connector
class envoie_planning():
    def __init__(self):
        #Lecture base de données
        ################################################################
        #Pour chaque étudiant de la base de donnée on fait : 

        mydb = mysql.connector.connect(
        host="localhost",
        user="hugodemenez",
        password="password",
        database="database",
        auth_plugin='mysql_native_password',
        )

        Liste = mydb.cursor()
        Liste.execute("SELECT * FROM user")


        for (username,password,email) in Liste:
            planning =scraping().get_planning(username = username,password = password)
            self.initialiser_csv('planning.csv')
            for i in planning:
                self.ajouter(i['cours'],i['date_debut'],i['heure_debut'],i['date_fin'],i['heure_fin'],i['professeur'],i['salle'],'planning.csv')
                #self.ajouter_calendrier_google(jour_et_heure_debut= i['date-google-api-debut'],jour_et_heure_fin = i['date-google-api-fin'],cours =i['cours'],professeur= i['professeur'],salle=i['salle'])
            self.envoyer_planning_email(destinataire=email)


    def initialiser_csv(self,chemin):
        fichier = open(chemin,"w")
        fichier.write("subject,Start Date,Start Time, End Date, End Time, Description,Location\n")
        fichier.close()

    def ajouter(self,cours,date_debut, heure_debut,date_fin,heure_fin,professeur,salle,chemin):
        fichier = open(chemin,"a")
        fichier.write("%s,%s,%s,%s,%s,%s,%s"%(cours,date_debut,heure_debut,date_fin,heure_fin,professeur,salle))
        fichier.write("\n")
        fichier.close()

    def envoyer_planning_email(self,destinataire):
        msg = MIMEMultipart()
        msg['From'] = 'ProjetInfoIsen2021@gmail.com' #adresse mail de départ, ici celle du projet
        msg['To'] = destinataire #destinataire
        msg['Subject'] = 'Emploi du temps semaine du ' + str(datetime.now().day) + '-' + str(datetime.now().month) + '-' + str(datetime.now().year) #objet du mail
        
        
        html_txt = ''

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

    def ajouter_calendrier_google(self,jour_et_heure_debut,jour_et_heure_fin,cours,professeur,salle):
        CLIENT_SECRET_FILE  = 'api.json'
        API_NAME = 'calendar'
        API_VERSION = 'v3'
        SCOPES = ['https://www.googleapis.com/auth/calendar']

        flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRET_FILE, SCOPES)
        cred = flow.run_local_server()
        service = build(API_NAME, API_VERSION, credentials=cred)
        evenement = {
        'summary': cours,
        'location': salle,
        'description': professeur,
        'start': {
            'dateTime': jour_et_heure_debut,
            'timeZone': 'Europe/Paris',
        },
        'end': {
            'dateTime': jour_et_heure_fin,
            'timeZone': 'Europe/Paris',
        }
        }
        service.events().insert(calendarId='primary', body=evenement).execute()

if __name__ == '__main':
    pass