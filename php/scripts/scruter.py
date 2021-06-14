import time
from commandes import complete_database,envoie_planning
from datetime import datetime
from time import strftime

class scan:
    def __init__(self):
        self.path = 'waiting_list.txt'
        fichier = open(self.path,"r")
        liste_init = []
        for ligne in fichier:
            liste_init.append(ligne)
        self.timer = 0
        self.scruter(liste_init)
        
    def scruter(self,liste):
        cst =0
        while True:
            if (datetime.now().strftime("%w")=="0") & (cst ==0): #si on est dimanche on envoie le planning,
                envoie_planning()                                   #on utilise une constante pour n'envoyer le mail qu'une fois
                cst=1
            if (datetime.now().strftime("%w")=="1"): 
                cst = 0

            new_liste = []
            fichier = open(self.path,"r")
            for ligne in fichier:
                new_liste.append(ligne)

            #Si les listes sont differentes alors quelqu'un s'est inscrit, on actualise la base de données
            if (new_liste != liste):
                complete_database()
                liste = new_liste
            fichier.close()

            #On complete la base de données toutes les 12heures même si personne s'est inscrit
            if self.timer >43200:
                complete_database()
                self.timer=0

            time.sleep(60)
            self.timer +=60

            


if __name__ == "__main__":
    scan()