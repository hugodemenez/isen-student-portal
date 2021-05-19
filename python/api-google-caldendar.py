from pprint import pprint
from google_auth_oauthlib.flow import Flow, InstalledAppFlow
from googleapiclient.discovery import build

class Calendrier():
    def __init__(self):
            self.CLIENT_SECRET_FILE  = r'C:\Users\Hugo\OneDrive\Github\Projet_2021_Informatique\json_files\code_secret_client_902657260294-uosch8kaf16e1tjuq18vvkdvov46hj0d.apps.googleusercontent.com.json'
            self.API_NAME = 'calendar'
            self.API_VERSION = 'v3'
            self.SCOPES = ['https://www.googleapis.com/auth/calendar']
            self.flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRET_FILE, SCOPES)
            self.cred = self.flow.run_local_server()
            self.service = build(API_NAME, API_VERSION, credentials=self.cred)

    def ajouter_event(date_google_api_debut,date_google_api_fin,cours,professeur,salle):
        try:

            event = {
            'summary': cours,
            'location': salle,
            'description': professeur,
            'start': {
                'dateTime': date_google_api_debut,
                'timeZone': 'Europe/Paris',
            },
            'end': {
                'dateTime': date_google_api_fin,
                'timeZone': 'Europe/Paris',
            }
            }
            event = service.events().insert(calendarId='primary', body=event).execute()
        except:
            pass

    def creer_calendrier():
        calendar = {
        'summary': 'ISEN COURS',
        }

        created_calendar = service.calendars().insert(body=calendar).execute()
        return (created_calendar['id'])

