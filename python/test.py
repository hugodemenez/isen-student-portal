import commandes,webscraping

user = webscraping.scraping().getting_identification_from_database()
print(webscraping.scraping().get_planning(username=user['username'],password=user['password']))
print(webscraping.scraping().get_marks(username=user['username'],password=user['password']))
commandes.envoie_planning()