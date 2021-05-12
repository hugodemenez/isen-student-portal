import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from webscrapping import scraping


class creation_fichier_ics():
    def __init__(self):
        planning =     scraping().get_planning(username = 'p64043',password = '7vBasPXs')
        self.initialiser_ics('planning.ics')
        for i in planning:
            self.ajouter_evenement(i["debut"],i["salle"],i["fin"],i["cours"],i["professeur"],'planning.ics')
        self.cloture_ics('planning.ics')

    def initialiser_ics(self,chemin): #on écrit le début d'un nouveau fichier
        fichier = open(chemin,"w")
        fichier.write('BEGIN:VCALENDAR\nVERSION:2.0\n')
        fichier.write('PRODID:-//hacksw/handcal//NONSGML v1.0//EN\n\n\n')
        fichier.write('BEGIN:VTIMEZONE\nTZID:Romance Standard Time\nBEGIN:STANDART\nDTSART:16011104T020000\nRRULE:FREQ=YEARLY;BYDAY=1SU;BYMONTH=11\n')
        fichier.write('TZOFFSETFROM:+0600\nTZOFFSETTO:+0500\nEND:STANDARD\n')
        fichier.write('BEGIN:DAYLIGHT\nDTSTART:16010311T020000\nRRULE:FREQ=YEARLY;BYDAY=2SU;BYMONTH=3\nTZOFFSETFROM:+0500\nTZOFFSETTO:+0800\nEND:DAYLIGHT\n')
        fichier.write('END:VTIMEZONE\n')
        fichier.close()

    def ajouter_evenement(self,debut,salle,fin,intitule,prof,chemin):    
        fichier = open(chemin,"a")
        fichier.write('BEGIN:VEVENT\n' + 'DTSTART;'+'TZID=Europe/Paris:'+debut+ '00\n' + 'DTEND;'+'TZID=Europe/Paris:'+fin+ '00\n' + 'LOCATION:'+salle+'\n' + 'SUMMARY:'+intitule+'\n' + 'CATEGORIES:cours' +'\n'
    + 'DESCRIPTION:' + prof + '\n' + 'END:VEVENT\n' )
        fichier.close()

    def cloture_ics(self,chemin): # on écrit les lignes de fin
        fichier = open(chemin,'a')
        fichier.write('\n\n\nEND:VCAlENDAR')
        fichier.close()

def envoie_mail(chemin,destinataire):
    expediteur = '' #adresse mail 
    message = MIMEMultipart()
    message['from'] = expediteur
    message['to'] = destinataire
    message['subject'] = 'Emploi du temps'

    html='''
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
    <title>Test email</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <head>
    <style>
    body {
    padding: 0 0 0 0;
    margin:0 0 0 0;
    }
    table{
    width : 100%;
    cellspaceing : 0;
    display: inline-table;
    border-collapse: collapse;
    }
    td,th {
    border: 1px solid black;	
    padding: 10px 10px 8px 5px;}
    p{
    color : white;
    }
    </style>
    </head>




    <body>
    <table cellspacing = 0 cellpadding = 0 >
    <tr><td bgcolor = "#FF0000	">
    <font size = "7" color = "white">
    <p>
    <b>
    <center>
    Emploi du temps de la semaine </center></td></tr>

    </p>
    </b>
    <tr><td><center>Importez le fichier .ics dans votre calendrier</center></td></tr>
        

    <table>	
    <body>'''    

    html_mime = MIMEText(html,'html')
    message.attach(html_mime)


    #pièce jointe
    fichier = open(chemin, "rb")
    part = MIMEBase ('application','octet-stream')
    part.set_playload((fichier).read())
    encoders.encode_base64(part)
    part.add_header('content-Disposition', "fichier; filename= %s"% chemin)
    msg.attach(part)
    #serveur
    serveur = smtplib.SMTP('smtp.gmail.com', 587)
    serveur.starttls()
    serveur.login(expediteur, "VOTRE MOT DE PASSE")
    texte= message.as_string().encode('utf-8')
    #envoi du mail  
    serveur.sendmail(expediteur,destinataire, message)
    serveur.quit()


if __name__ == '__main':
    pass