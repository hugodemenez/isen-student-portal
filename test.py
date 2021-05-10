debut = '20210511T1700'
fin = '20210511T1730'
salle = 'B502'
intitule = 'maths'
prof = 'chenevert'


fichier = open('C:/Users/brieu/Desktop/calend.ics',"a")

fichier.write('BEGIN:VCALENDAR\nVERSION:2.0\n')
fichier.write('PRODID:-//hacksw/handcal//NONSGML v1.0//EN\n\n\n')

fichier.write('BEGIN:VEVENT\n' + 'DTSTAT:'+debut+ '00Z\n' + 'DTEND:'+fin+ '00Z\n' + 'LOCATION:'+salle+'\n' + 'SUMMARY:'+intitule+'\n' + 'CATEGORIES:cours' +'\n'
 + 'DESCRPTION:' + prof + '\n' + 'END:VEVENT\n' )
fichier.write('\n\n\nEND:VCAlENDAR')
fichier.close()

