import pyttsx3


engine = pyttsx3.init('sapi5')

def speak(audio):
    print('Computer: ' + audio)
    engine.say(audio)
    engine.runAndWait()
speak('je vais au parc.')

# pyttsx3.init('sapi5').say('bite')
# pyttsx3.init('sapi5').runAndWait()


