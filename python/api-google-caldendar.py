from pprint import pprint
from Google import Create_Service
CLIENT_SECRET_FILE  = 'C:/Users/brieu/Desktop/code_secret_client_902657260294-uosch8kaf16e1tjuq18vvkdvov46hj0d.apps.googleusercontent.com.json'
API_NAME = 'calendar'
API_VERSION = 'v3'
SCOPES = ['https://www.googleapis.com/auth/calendar']



service = Create_Service (CLIENT_SECRET_FILE,API_NAME, API_VERSION, SCOPES)

def ajouter_event(jour_et_heure_debut,jour_et_heure_fin,intitule,prof,salle,):
    evenement = {
    'summary': intitule,
    'location': salle,
    'description': prof,
    'start': {
        'dateTime': jour_et_heure_debut,
        'timeZone': 'Europe/Paris',
    },
    'end': {
        'dateTime': jour_et_heure_fin,
        'timeZone': 'Europe/Paris',
    }
    }

    event = service.events().insert(calendarId='primary', body=evenement).execute()

