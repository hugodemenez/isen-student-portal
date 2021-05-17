from pprint import pprint
from Google import Create_Service
CLIENT_SECRET_FILE  = 'C:/Users/brieu/Desktop/code_secret_client_902657260294-uosch8kaf16e1tjuq18vvkdvov46hj0d.apps.googleusercontent.com.json'
API_NAME = 'calendar'
API_VERSION = 'v3'
SCOPES = ['https://www.googleapis.com/auth/calendar']



service = Create_Service (CLIENT_SECRET_FILE,API_NAME, API_VERSION, SCOPES)



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
  },
}

event = service.events().insert(calendarId='primary', body=event).execute()

