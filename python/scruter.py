import time #chemin est la variable qui donne l'emplacement du fichier à vérifier
def init(chemin):
    fichier = open(chemin,"r")
    liste_test = []
    for ligne in fichier:
        liste_test.append(ligne)
    return liste_test

def scruter(liste_test,chemin):
    while True:
        liste = []
        fichier = open(chemin,"r")
        for ligne in fichier:
            liste.append(ligne)
        if (liste != liste_test):
            #action à exécuter
            print("ok")

            liste_test = liste
        fichier.close()
        time.sleep(3600) #on attend 1 heure


# liste_test = init()
# print(liste_test)
# time.sleep(60)
# scruter(liste_test)