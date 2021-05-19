import commandes,webscraping



#print(webscraping.scraping().get_planning( username = 'p64059',password = 'ny5mJb8z'))

from pprint import pprint
from google_auth_oauthlib.flow import Flow, InstalledAppFlow
from googleapiclient.discovery import build



CLIENT_SECRET_FILE  = r'C:\Users\Hugo\OneDrive\Github\Projet_2021_Informatique\python\api.json'
API_NAME = 'calendar'
API_VERSION = 'v3'
SCOPES = ['https://www.googleapis.com/auth/calendar']


flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRET_FILE, SCOPES)
cred = flow.run_local_server()
service = build(API_NAME, API_VERSION, credentials=cred)




event = {
  'summary': 'repas',
  'location': 'maison',
  'description': 'A table',
  'start': {
    'dateTime': '2021-05-18T12:00:00+02:00',
    'timeZone': 'Europe/Paris',
  },
  'end': {
    'dateTime': '2021-05-18T13:30:00+02:00',
    'timeZone': 'Europe/Paris',
  }
}

event = service.events().insert(calendarId='primary', body=event).execute()