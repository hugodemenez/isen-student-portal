import speech_recognition as sr



def commandeinter():
    try:
        r = sr.Recognizer()                                                                                   
        with sr.Microphone() as source:                                                                       
            print("Listening...")
            r.pause_threshold =  1
            audio = r.listen(source)
            query = r.recognize_google(audio, language='fr-in')
            print('User: ' + query + '\n')
    except:
        query=OK()
        return query


def OK():
    query=commandeinter()
    return query
    
    
a=OK()


