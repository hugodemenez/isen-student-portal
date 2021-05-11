from seleniumwire import webdriver  # Import from seleniumwire
from selenium.webdriver.firefox.options import Options
from time import sleep
import json



class Planning():
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

    def get(self,username,password):
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

                    #On retire les informations qui ne nous interessent pas
                    dict.pop('id', None)
                    dict.pop('allDay', None)
                    dict.pop('editable', None)
                    #On ajoute le dictionnaire à la liste
                    data.append(dict)
            except Exception as error:
                print(error)
                pass


        return data








if __name__ == "__main__":
    identification = Planning().getting_identification_from_database()
    planning = Planning().get(username=identification['username'],password=identification['password'])
    print(planning)