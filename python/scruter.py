import time #chemin est la variable qui donne l'emplacement du fichier à vérifier
from commandes import complete_database


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
        while True:
            liste = []
            fichier = open(self.path,"r")
            for ligne in fichier:
                liste.append(ligne)

            #On regarde si les listes sont différentes
            if (liste != liste_test):
                complete_database()
                liste_test = liste
            fichier.close()
            if self.timer >60:
                complete_database()
                self.timer=0
            
            


# liste_test = init()
# print(liste_test)
# time.sleep(60)
# scruter(liste_test)