import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def initialiser_ics(chemin): #on écrit le début d'in nouveau fichier
    fichier = open(chemin,"w")
    fichier.write('BEGIN:VCALENDAR\nVERSION:2.0\n')
    fichier.write('PRODID:-//hacksw/handcal//NONSGML v1.0//EN\n\n\n')
    fichier.close()

def ajouter_evenement(debut,salle,fin,intitule,prof,chemin): #pour ajouter un évènement dates = (année mois jour heure minute)
    fichier = open(chemin,"a")
    fichier.write('BEGIN:VEVENT\n' + 'DTSTART:'+debut+ '00Z\n' + 'DTEND:'+fin+ '00Z\n' + 'LOCATION:'+salle+'\n' + 'SUMMARY:'+intitule+'\n' + 'CATEGORIES:cours' +'\n'
 + 'DESCRPTION:' + prof + '\n' + 'END:VEVENT\n' )
    fichier.close()

def cloture_ics(chemin): # on écrit les lignes de fin
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
<table>
<table cellspacing = 0>
<table cellpadding = 0>

<tr><td bgcolor = "#FF0000	">
<font size = "7">
<p>
<b>
Emploi du temps de la semaine</td></tr>
</p>
</b>
<tr><td> </td></tr>
	

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
    serveur.sendmail(expediteur, Toaddestinataired, message.as_string)
    serveur.quit()