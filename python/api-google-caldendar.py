from google_auth_oauthlib.flow import Flow, InstalledAppFlow
from googleapiclient.discovery import build


CLIENT_SECRET_FILE  = 'C:/Users/brieu/Desktop/code_secret_client_902657260294-uosch8kaf16e1tjuq18vvkdvov46hj0d.apps.googleusercontent.com.json'
API_NAME = 'calendar'
API_VERSION = 'v3'
SCOPES = ['https://www.googleapis.com/auth/calendar']

flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRET_FILE, SCOPES)
cred = flow.run_local_server()
service = build(API_NAME, API_VERSION, credentials=cred)

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

    service.events().insert(calendarId='primary', body=evenement).execute()

