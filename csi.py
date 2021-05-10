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
    envoyeur = '' #adresse mail
    message = MIMEMultipart()
    message['from'] = envoyeur
    message['to'] = destinataire
    message['subject'] = 'Emploi du temps'
    message = 'Emploi du temps de la semaine'
    #pièce jointe
    fichier = open(chemin, "rb")
    part = MIMEBase ('application','octet-stream')
    part.set_playload((fichier).read())
    encoders.encode_base64(part)
    part.add_header('content-Disposition', "fichier; filename= %s"% chemin)
    msg.attach(part)
    #envoi du mail
    serveur = smtplib.SMTP('smtp.gmail.com', 587)
    serveur.starttls()
    serveur.login(Fromadd, "VOTRE MOT DE PASSE")
    texte= message.as_string().encode('utf-8')
    serveur.sendmail(Fromadd, Toadd, texte)
    serveur.quit()

