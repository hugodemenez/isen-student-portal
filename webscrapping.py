from seleniumwire import webdriver  # Import from seleniumwire
from selenium.webdriver.firefox.options import Options
from time import sleep
import json
import re



class scraping():
    """
    Cette classe regroupe les differentes fonctions de scraping utilisées pour récuperer les données de WebAurion
    """
    def __init__(self):
        #Configuration du Headless Webbrowser
        self.options = Options()
        self.options.headless = True
        self.options.binary_location = r"C:\Program Files\Mozilla Firefox\firefox.exe"
        self.driver = webdriver.Firefox(options=self.options, executable_path="geckodriver.exe")

    def getting_identification_from_database(self):
        #Exemple avec un utilisateur
        username = 'p64059'
        password = 'ny5mJb8z'
        email = 'hugo.demenez@isen.yncrea.fr'
        dict = {
            'username':username,
            'password':password,
            'email':email
            }
        return dict

    def get_planning(self,username,password):
        """
        Cette fonction sert à récuperer une liste des différents cours sous forme de dictionnaires avec :
        dictionnaire["salle"],
        dictionnaire["professeur"],
        dictionnaire["debut"],
        dictionnaire["fin"],
        dictionnaire["cours"]
        """
        #Ouverture de la page de connexion aurion
        self.driver.get('https://aurion.junia.com/faces/Login.xhtml')

        #Remplissage du nom utilisateur
        inputElement = self.driver.find_element_by_id("username")
        inputElement.send_keys(username)

        #Remplissage du mot de passe
        inputElement = self.driver.find_element_by_id("password")
        inputElement.send_keys(password)

        #Validation des données d'identification
        inputElement.submit() 

        #Recherche de la zone pour acceder au planning
        counter=0
        while(True):
            
            try:
                inputElement =self.driver.find_element_by_link_text("Mon Planning")
                break
            except:
                sleep(1)
                if counter == 10:
                    raise Exception("Unable to load schedule")
                counter+=1
                pass

        #Une fois la zone selectionnée : on clique dessus
        inputElement.click() 

        #On attends que les requetes soient toutes soumises
        sleep(5)

        #On accède aux requetes envoyées par le HeadlessWebbrowser
        for request in self.driver.requests:
            #S'il y a une reponse
            if request.response:
                #On verifie que la reponse correspond bien au planning
                if 'Planning' in request.url :
                    if 'POST' in request.method:
                        response = request.response.body
                        response=str(response)


        #On met en forme la reponse pour pouvoir créer une liste de dictionnaires
        response = response[response.find('events')+11:].strip()
        response = response[:response.find(']}]]')].strip()
        response = response+','
        response = response.split("{")

        #On initialise la liste
        data=[]

        for elem in response:
            try:
                if elem !='':
                    #On remet en forme le string pour être traduit en dictionnaire
                    string_dict = '{'+elem
                    string_dict=string_dict[:-1]
                    string_dict=string_dict.replace("\\\\n", " ") 
                    string_dict=string_dict.replace("\\xc3\\xa9", "e") 

                    #On traduit le string en dictionnaire
                    dict=json.loads(string_dict)

                    #On initialise le dictionnaire à renvoyer
                    dictionnaire={}

                    #On traite les infos pour récuperer ce qui nous interesse
                    salle = re.match("[a-zA-Z0-9]+[ ][a-zA-Z0-9]+[ (H)]+",dict["title"][3:]).group()
                    cours = re.match("[a-zA-Z ]+",dict["title"][(3+len(salle)):]).group()
                    professeur = re.match("[A-Za-z ]+",dict["title"][17+len(salle)+len(cours):]).group()

                    #On recupere les horaires dans le format nécessaire pour le calendrier
                    liste_debut = re.findall("[0-9]+",dict["start"])
                    liste_fin = re.findall("[0-9]+",dict["end"])
                    heure_debut=''
                    heure_fin=''
                    liste_fin[2]+='T'
                    liste_debut[2]+='T'
                    for i in range(5):
                        heure_debut+=liste_debut[i]
                        heure_fin+=liste_fin[i]


                    #On reformule le dictionnaire avec les informations classées
                    dictionnaire["salle"]=salle
                    dictionnaire["professeur"] = professeur
                    dictionnaire["debut"] = heure_debut
                    dictionnaire["fin"] = heure_fin
                    dictionnaire["cours"] = cours

                    #On ajoute le dictionnaire à la liste qui contient les differents cours de la semaine
                    data.append(dictionnaire)
            except Exception as error:
                print(error)
                pass


        return data








if __name__ == "__main__":
    identification = Planning().getting_identification_from_database()
    planning = Planning().get(username=identification['username'],password=identification['password'])
    print(planning)