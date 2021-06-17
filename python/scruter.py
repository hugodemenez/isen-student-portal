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
                    liste = new_liste
            fichier.close()

            #On complete la base de données toutes les 12heures même si personne s'est inscrit
            if self.timer >3600:
                Liste = self.database.cursor()
                Liste.execute("SELECT * FROM user")
                for (username,password,email) in Liste:
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
                        self.notification_data(email)
                self.timer=0

            time.sleep(1)
            self.timer +=1

    def notification_marks(self,email):
        msg = MIMEMultipart()
        msg['From'] = 'ProjetInfoIsen2021@gmail.com' #adresse mail de départ, ici celle du projet
        msg['To'] = email #destinataire
        msg['Subject'] = "ISENINFO - Notification" #objet du mail
        #Message du mail
        html_txt = '<h1>Vous avez une nouvelle note</h1>'

        msg.attach(MIMEText(html_txt,'html'))
        mailserver = smtplib.SMTP('smtp.gmail.com', 587)    #serveur et numéro du port pour envoyer le mail
        mailserver.ehlo()
        mailserver.starttls()
        mailserver.ehlo()
        mailserver.login('ProjetInfoIsen2021@gmail.com', 'gloubiboulga1') #on se connecte au compte gmail pour envoyer le mail
        mailserver.sendmail('ProjetInfoIsen2021@gmail.com', email, msg.as_string()) #on envoie le mail
        mailserver.quit()

    def notification_planning(self,email):
        msg = MIMEMultipart()
        msg['From'] = 'ProjetInfoIsen2021@gmail.com' #adresse mail de départ, ici celle du projet
        msg['To'] = email #destinataire
        msg['Subject'] = "ISENINFO - Notification" #objet du mail
        #Message du mail
        html_txt = '<h1>Vous avez une changement dans votre planning</h1>'

        msg.attach(MIMEText(html_txt,'html'))
        mailserver = smtplib.SMTP('smtp.gmail.com', 587)    #serveur et numéro du port pour envoyer le mail
        mailserver.ehlo()
        mailserver.starttls()
        mailserver.ehlo()
        mailserver.login('ProjetInfoIsen2021@gmail.com', 'gloubiboulga1') #on se connecte au compte gmail pour envoyer le mail
        mailserver.sendmail('ProjetInfoIsen2021@gmail.com', email, msg.as_string()) #on envoie le mail
        mailserver.quit()

    def notification_data(self,email):
        msg = MIMEMultipart()
        msg['From'] = 'ProjetInfoIsen2021@gmail.com' #adresse mail de départ, ici celle du projet
        msg['To'] = email #destinataire
        msg['Subject'] = "ISENINFO - Notification" #objet du mail
        #Message du mail
        html_txt = '<h1>Vous pouvez dès à présent consulter votre planning et vos notes sur notre site</h1>'

        msg.attach(MIMEText(html_txt,'html'))
        mailserver = smtplib.SMTP('smtp.gmail.com', 587)    #serveur et numéro du port pour envoyer le mail
        mailserver.ehlo()
        mailserver.starttls()
        mailserver.ehlo()
        mailserver.login('ProjetInfoIsen2021@gmail.com', 'gloubiboulga1') #on se connecte au compte gmail pour envoyer le mail
        mailserver.sendmail('ProjetInfoIsen2021@gmail.com', email, msg.as_string()) #on envoie le mail
        mailserver.quit()
            


if __name__ == "__main__":
    scan()