def initialiser_ics(chemin): #on écrit le début d'in nouveau fichier
    fichier = open(chemin,"w")
    fichier.write('BEGIN:VCALENDAR\nVERSION:2.0\n')
    fichier.write('PRODID:-//hacksw/handcal//NONSGML v1.0//EN\n\n\n')
    fichier.close()

def ajouter_evenement(debut,salle,fin,intitule,prof,chemin): #pour ajouter un évènement dates = (année mois jour heure minute)
    fichier = open(chemin,"a")
    fichier.write('BEGIN:VEVENT\n' + 'DTSTAT:'+debut+ '00Z\n' + 'DTEND:'+fin+ '00Z\n' + 'LOCATION:'+salle+'\n' + 'SUMMARY:'+intitule+'\n' + 'CATEGORIES:cours' +'\n'
 + 'DESCRPTION:' + prof + '\n' + 'END:VEVENT\n' )
    fichier.close()

def cloture_ics(chemin): # on écrit les lignes de fin
    fichier = open(chemin,'a')
    fichier.write('\n\n\nEND:VCAlENDAR')
    fichier.close()