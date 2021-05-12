import re

dict={}
dict['title']=' - ISEN B802     (H) Projet Developpement Logiciel 08:00 - 12:00 Monsieur LEFETZ'

"""
[{'title': ' - ISEN B802     (H) Projet Developpement Logiciel 08:00 - 12:00 Monsieur LEFETZ', 
'start': '2021-05-10T08:00:00+0200', 
'end': '2021-05-10T12:00:00+0200', 
'className': 'PROJET'}]
"""
mobj1 = re.match("[a-zA-Z0-9]+[ ][a-zA-Z0-9]+[ (H)]+",dict["title"][2:]).group()