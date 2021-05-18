import sqlite3

connexion = sqlite3.connect("python/database.db")

cursor = connexion.cursor()

#Add user to user table :
username = 'p63058'
password = 'vYYuQxIx'
email = 'guillaume.gulli@isen.yncrea.fr'


parametres = (username,password,email)
command = "INSERT OR REPLACE INTO user VALUES (?,?,?)"
cursor.execute(command,parametres)
connexion.commit()



cursor.execute("SELECT * FROM user")
print(cursor.fetchall())