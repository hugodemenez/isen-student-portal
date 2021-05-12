import wikipedia
import pyttsx3

engine = pyttsx3.init('sapi5')

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[len(voices)-1].id)
def speak(audio):
    print('Computer: ' + audio)
    engine.say(audio)
    engine.runAndWait()


results = wikipedia.summary('python', sentences=5)
speak(results)