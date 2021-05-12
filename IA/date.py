import datetime
import pyttsx3

engine = pyttsx3.init('sapi5')



voices = engine.getProperty('voices')
engine.setProperty('voice', voices[len(voices)-1].id)

def speak(audio):
    print('Computer: ' + audio)
    engine.say(audio)
    engine.runAndWait()
    
# def greetMe():
#     currentH = int(datetime.datetime.now().hour)
#     if currentH >= 0 and currentH < 12:
#         speak('Bonjour Hakim!')
# 
#     if currentH >= 12 and currentH < 18:
#         speak('Bonjour Hakim!')
# 
#     if currentH >= 18 and currentH !=0:
#         speak('Bonsoir Hakim!')


a=datetime.datetime.now().hour
speak(a)