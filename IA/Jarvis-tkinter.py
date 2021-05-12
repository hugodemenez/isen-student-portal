import pyttsx3
import webbrowser
import random
import speech_recognition as sr
import wikipedia
import datetime
import os
import sys
import time
from tkinter import *

tk=Tk()
canvas=Canvas(tk, height=600,  width=600  , bg="white")
canvas.pack()
pointcrane1=[240,567,360,567,520,400,520,300,500,267,520,100.5,400,34,200,34,80,100.5,100,267,80,300.3,80,300.3,80,400.2,240,566.7]
pointoeilg=[220,300.3,140,290.3,152,270.3,208,257,240,283.65,220,300.3]
pointoeild=[380,300.3,460,290.3,448,270.3,392,257,360,283.6,380,300.3]
pointbouche1=[240,500,360,500,400,466.8,360,433.5,300,450.15,240,433.5,200,466.8,400,466.8,200,466.8,240,500]
pointcrane2=[200,566.7,400,566.7,520,400.2,520,300.3,500,267,520,100.5,400,33.9,200,33.9,80,100.5,100,267,80,300.3,80,400.2,200,566.7]
pointbouche2=[200,466.8,240,423.5,300,433.5,360,423.5,400,466.8,360,456.8,240,456.8,200,466.8,240,516.7,360,516.75,400,466.8,360,483.45,240,483.45,200,466.8]



engine = pyttsx3.init('sapi5')

def parler():
    i=0
    while i!=3:
        for i in range (4):
            canvas.create_polygon(pointcrane2, fill='white', outline='white', width=4)
            crane1=canvas.create_polygon(pointcrane1, fill='white', outline='black', width=4)
            oeilg=canvas.create_polygon(pointoeilg, fill='white', outline='black', width=4)
            oeild=canvas.create_polygon(pointoeild, fill='white', outline='black', width=4)
            bouche1=canvas.create_polygon(pointbouche1, fill='white', outline='black', width=4)
            tk.update()
            time.sleep(1)
            crane1=canvas.create_polygon(pointcrane1, fill='white', outline='white', width=4)
            crane2=canvas.create_polygon(pointcrane2, fill='white', outline='black', width=4)
            bouche2=canvas.create_polygon(pointbouche2, fill='white', outline='black', width=4)
            oeilg=canvas.create_polygon(pointoeilg, fill='white', outline='black', width=4)
            oeild=canvas.create_polygon(pointoeild, fill='white', outline='black', width=4)
            tk.update()
            time.sleep(0.5)

def speak(audio):
    parler()
    print(audio)

def greetMe():
    currentH = int(datetime.datetime.now().hour)
    if currentH >= 0 and currentH < 18:
        speak('Bonjour Hakim!')
    else :
        speak('Bonsoir Hakim!')

def commandeinter():
    try:
        r = sr.Recognizer()                                                                                   
        with sr.Microphone() as source:                                                                       
            print("Listeningg...")
            r.pause_threshold =  1
            audio = r.listen(source)
            query = r.recognize_google(audio, language='fr-in')
            print('User: ' + query + '\n')
    except:
        query=myCommand()
    return query

def myCommand():
    tk.destroy()
    query=commandeinter()
    
    return query
    



greetMe()
# print('attente activation. . .')
# query=myCommand()

# while ('Jarvis' not in  query) and ('activation' not in query) and ('active' not in query):
#     query=myCommand()
#     print('attente activation. . .')
# speak('Que puis-je faire pour vous?')



while True:

    query = myCommand()
    a=0
    
    if 'ouvre youtube' in query:
        webbrowser.open('www.youtube.com')

    elif 'ouvre google' in query:
        webbrowser.open('www.google.com')

    elif 'ouvre gmail' in query or 'ouvre mes mail' in query :
        webbrowser.open('www.gmail.com')

    elif 'vas' in query and 'tu' in query or 'va' in query and 'tu' in query:
        stMsgs = ['bien et vous!','fatigué, pouvez vous rebranchez mon chargeur!', 'je suis remplis dénergies']
        speak(random.choice(stMsgs))

    elif 'arret' in query or 'arretes' in query or 'stop' in query or query=='merci' :
        speak('ok')
        speak('Bonne journée.')
        sys.exit()
        
    elif 'quelle heure est-il' in query:
        speak('il est')
        pyttsx3.init('sapi5').say(datetime.datetime.now().hour)
        pyttsx3.init('sapi5').runAndWait()
        speak('heur')
    
    
    elif 'musique' in query or 'morceau' in query:
        music1=['C:/Users/Hakim/Desktop/Music/westworld-season-2-heart-shaped-box-ramin-djawadi-official.mp3','C:/Users/Hakim/Desktop/Music/ultimate-gaming-music-mix-2015-electrohousedubstep-dropsdrumstep.mp3','C:/Users/Hakim/Desktop/Music/official-westworld-soundtrack-paint-it-black-ramin-djawadi.mp3','C:/Users/Hakim/Desktop/Music/game-of-thrones-season-6-ost-02-blood-of-my-blood.mp3','C:/Users/Hakim/Desktop/Music/westworld-season-2-heart-shaped-box-ramin-djawadi-official.mp3']
        music2=random.choice([music1[0],music1[1],music1[2],music1[3],music1[4]])
        os.system(music2)
        speak('Voici votre music! Enjoy!')
    
    elif ('recherche' in query or 'cherche' in query):
            try:
                speak('que voulez vous rechercher? ')
                content = myCommand()
                site=['&oq=&gs_l=psy-ab.1.2.35i39l6.0.0..10558...2.0..0.318.318.3-1......0......gws-wiz.....6.X_oDmQRq4Zo']
                site.append(content)
                site.append('https://www.google.com/search?source=hp&ei=rrTSXKHVKtOHjLsP_4GQuAo&q=')
                site2=site[2]+site[1]+site[0]
                print(site2)
                webbrowser.open(site2)
            except:
                speak('Désolé Monsieur je suis dans lincapacité de vous aider!')
                
    elif 'note'in query or 'mémo' in query:
        speak('que voulez vous écrire? ')
        text = myCommand()
        open("C:/Users/Hakim/Desktop/note.txt", "a") .write('\n' + text)
        speak('Jen prends note')
    
    elif 'apprend' in query:
        speak('que voulez vous mapprendre?')
        print('question...')
        text=myCommand()
        open("C:/Users/Hakim/Desktop/question.txt", "a") .write('\n' + text)
        speak('daccord et que dois-je répondre')
        text=myCommand()
        open("C:/Users/Hakim/Desktop/rep.txt", "a") .write('\n' + text)
        speak('merci monsieur')
    
    
    elif 'calcul' in query:
        try:
            speak('quelle opération dois-je résoudre?')
            a=myCommand().split(" ")
            c=a[0]
            del(a[0])
            for i in range(int((len(a)-1)/2)+1):
                b=[a[0],a[1]]
                if b[0]=='x':
                    c=float(c)*int(b[1])
                elif b[0]=='/':
                    c=float(c)/int(b[1])
                del(a[0], a[0])
            speak('égale')
            speak(str(c))
        except:
            speak('oulala cela me parait compliqué')
        
    else:
        a=1
        
        
    for ligne in open("C:/Users/Hakim/Desktop/question.txt","rU"):
        ligne=open("C:/Users/Hakim/Desktop/question.txt","rU").readlines()
    for lignerep in open("C:/Users/Hakim/Desktop/rep.txt","rU"):
        lignerep=open("C:/Users/Hakim/Desktop/rep.txt","rU").readlines()
    for i in range (len(ligne)):
        ligne[i]=ligne[i][0:-1]
        if ligne[i] in query :
            speak(lignerep[i])
            a=0
        
    
    if a == 1:
        speak('Recherche...')
        try:
            
            results = wikipedia.summary(query, sentences=5)
            speak('Jai, selon WIKIPEDIA  ')
            voices = pyttsx3.init('sapi5').getProperty('voices')
            pyttsx3.init('sapi5').setProperty('voice', voices[len(voices)-1].id)
            speak(results)
            voices = pyttsx3.init('sapi5').getProperty('voices')
            pyttsx3.init('sapi5').setProperty('voice', voices[len(voices)-4].id)
    
        except:
            
            speak('Désolé Monsieur je suis dans lincapacité de vous aider!')
            
        

    speak('A votre service Monsieur')
    time.sleep(2)
