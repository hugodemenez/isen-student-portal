from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import smtplib
from datetime import datetime
from webscraping import scraping


class envoie_planning():
    def __init__(self):
        #Lecture base de données
        ################################################################
        #Pour chaque étudiant de la base de donnée on fait : 
        Liste=[]
        exemple = {
            "username" :'p64043',
            "password":'7vBasPXs',
            "email":"hugo.demenez@isen.yncrea.fr",
        }
        Liste.append(exemple)


        for student in Liste:
            planning =scraping().get_planning(username = student['username'],password = student['password'])
            self.initialiser_csv('planning.csv')
            for i in planning:
                self.ajouter(i['cours'],['date_debut'],['heure_debut'],['date_fin'],['heure_fin'],['professeur'],['salle'],'planning.csv')
            self.envoyer_planning_email(destinataire=student['email'])


    def initialiser_csv(self,chemin):
        fichier = open(chemin,"w")
        fichier.write("subject,Start Date,Start Time, End Date, End Time, Description,Location\n")
        fichier.close()

    def ajouter(self,cours,date_debut, heure_debut,date_fin,heure_fin,professeur,salle,chemin):
        fichier = open(chemin,"a")
        fichier.write("%s,%s,%s,%s,%s,%s,%s"%(cours,date_debut,heure_debut,date_fin,heure_fin,professeur,salle))
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


if __name__ == '__main':
    pass