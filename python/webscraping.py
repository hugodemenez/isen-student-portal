from seleniumwire import webdriver
from selenium.webdriver.firefox.options import Options
from time import sleep
import json
import re



class scraping():
    """
    Cette classe regroupe les differentes fonctions de scraping utilisées pour récuperer les données de WebAurion
    """
    def __init__(self):
        pass


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
        #Configuration du Headless Webbrowser
        options = Options()
        options.headless = True
        options.binary_location = r"C:\Program Files\Mozilla Firefox\firefox.exe"
        driver = webdriver.Firefox(options=options, executable_path="geckodriver.exe")
        #Ouverture de la page de connexion aurion
        driver.get('https://aurion.junia.com/faces/Login.xhtml')

        #Remplissage du nom utilisateur
        inputElement = driver.find_element_by_id("username")
        inputElement.send_keys(username)

        #Remplissage du mot de passe
        inputElement = driver.find_element_by_id("password")
        inputElement.send_keys(password)

        #Validation des données d'identification
        inputElement.submit() 

        #Recherche de la zone pour acceder au planning
        counter=0
        while(True):
            
            try:
                inputElement =driver.find_element_by_link_text("Mon Planning")
                break
            except:
                sleep(1)
                if counter == 10:
                    raise Exception("Unable to load schedule")
                counter+=1
                pass
        

        while(True):
            try:
                #Une fois la zone selectionnée : on clique dessus
                inputElement.click() 
                #On accède aux requetes envoyées par le HeadlessWebbrowser
                for request in driver.requests:
                    #S'il y a une reponse
                    if request.response:
                        #On verifie que la reponse correspond bien au planning
                        if 'Planning' in request.url :
                            if 'POST' in request.method:
                                response = request.response.body
                                response=str(response)
                
                break
            except:
                sleep(1)
                        
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


                    #pour les fichiers csv
                    date_buffer_debut =  re.search("[0-9-]+[0-9]+",dict["start"]).group()
                    date_debut= re.sub("[-]",'/', date_buffer_debut)

                    heure_debut=re.search("[0-9:]{5}",dict["start"]).group()

                    date_buffer_fin = re.search("[0-9-]+[0-9]+",dict["end"]).group()
                    date_fin=re.sub("[-]",'/', date_buffer)

                    heure_fin=re.search("[0-9:]{5}",dict["end"]).group()

                    #pour api google agenda
                    heure_et_jour_debut = date_buffer_debut + 'T' + heure_debut + '+02:00'
                    heure_et_jour_fin = date_buffer_fin + 'T' + heure_fin + '+02:00'



                    #On reformule le dictionnaire avec les informations classées
                    dictionnaire["salle"]=salle
                    dictionnaire["professeur"] = professeur
                    dictionnaire["date_debut"] = date_debut
                    dictionnaire["heure_debut"] = heure_debut
                    dictionnaire["date_fin"] = date_fin
                    dictionnaire["heure_fin"] = heure_fin
                    dictionnaire["cours"] = cours
                    dictionnaire["date-google-api-debut"] = heure_et_jour_debut
                    dictionnaire["date-google-api-fin"] = heure_et_jour_debut

                    #On ajoute le dictionnaire à la liste qui contient les differents cours de la semaine
                    data.append(dictionnaire)
            except Exception as error:
                print(error)
                pass
        driver.quit()

        return data

    def get_marks(self,username,password):
        #Configuration du Headless Webbrowser
        options = Options()
        options.headless = True
        options.binary_location = r"C:\Program Files\Mozilla Firefox\firefox.exe"
        driver = webdriver.Firefox(options=options, executable_path="geckodriver.exe")
        #Ouverture de la page de connexion aurion
        driver.get('https://aurion.junia.com/faces/Login.xhtml')

        #Remplissage du nom utilisateur
        inputElement = driver.find_element_by_id("username")
        inputElement.send_keys(username)

        #Remplissage du mot de passe
        inputElement = driver.find_element_by_id("password")
        inputElement.send_keys(password)

        #Validation des données d'identification
        inputElement.submit() 
        

        #Recherche de la zone pour acceder au planning
        counter=0
        while(True):
            
            try:
                inputElement =driver.find_element_by_link_text("Scolarité")
                break
            except:
                sleep(1)
                if counter == 10:
                    raise Exception("Unable to load schedule")
                counter+=1
                pass

        #Une fois la zone selectionnée : on clique dessus
        inputElement.click() 

        #Recherche de la zone pour acceder au planning
        counter=0
        while(True):
            
            try:
                inputElement =driver.find_element_by_link_text("Mes notes")
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
        for request in driver.requests:
            #S'il y a une reponse
            if request.response:
                #On verifie que la reponse correspond bien au planning
                if 'Notation' in request.url :
                    if 'GET' in request.method:
                        response = request.response.body
                        response=str(response)

        
        #On met en forme la reponse pour pouvoir créer une liste de dictionnaires

            #On recupere le contenu du body
        response = response[response.find('</thead>'):].strip()
        response = response[:response.find('</tbody>')].strip()
            #On recupere seulement le text present dans le body (on retire les balises)
        response = re.sub('<[^>]+>', '', response)

        #On retire les caractères spéciaux
        response=response.replace(r"\xc3\xa8", "e") 
        response=response.replace(r"\xc3\xa9", "e") 
        response=response.replace(r"\xc2\xb0", "O")
        response=response.replace(r"\xc3\xb4", "o")
        response=response.replace(r"\xc3\xa7", "c")
        response=response.replace(r"\'", "'")

        #On decoupe les resultats à chaque fois que l'on dispose d'une date sous la forme : D/M/Y
        responses = re.split('[0-9/]{10}', response)
        

        notes = []
        for response in responses:
            try:
                #On recupère la note et l'intitulé de la matère
                note = re.search("[0-9]{1,2}[.][0-9]{2}",response).group()
                matiere = re.sub("[a-z]+",'',response.split(' ', 1)[0])[:-1]
                #On ajoute le dictionnaire dans une liste que l'on renvoit par la suite
                notes.append({'matiere':matiere,'note':note})
            except:
                pass
        

        driver.quit()

        return notes

        







if __name__ == "__main__":
    user = scraping().getting_identification_from_database()
    scraping().get_planning(user['username'],user['password'])