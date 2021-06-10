import time #chemin est la variable qui donne l'emplacement du fichier à vérifier
from commandes import complete_database


class scan:
    def __init__(self):
        self.path = '/home/ubuntu/waiting_list.txt'
        fichier = open(self.path,"r")
        liste_init = []
        for ligne in fichier:
            liste_init.append(ligne)
        self.timer = 0
        self.scruter(liste_init)
        
    def scruter(self,liste):
        while True:
            liste = []
            fichier = open(self.path,"r")
            for ligne in fichier:
                liste.append(ligne)

            #Si les listes sont differentes alors quelqu'un s'est inscrit, on actualise la base de données
            if (liste != liste_test):
                complete_database()
                liste_test = liste
            fichier.close()

            #On complete la base de données toutes les 12heures même si personne s'est inscrit
            if self.timer >43200:
                complete_database()
                self.timer=0

            time.sleep(60)
            self.timer +=60
            
            


if __name__ == "__main__":
    scan()