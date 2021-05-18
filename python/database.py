import sqlite3

connexion = sqlite3.connect("python/database.db")

cursor = connexion.cursor()

#Add user to user table :
username = 'p64059'
password = 'ny5mJb8z'
email = 'hugo.demenez@isen.yncrea.fr'


parametres = (username,password,email)
command = "INSERT OR REPLACE INTO user VALUES (?,?,?)"
cursor.execute(command,parametres)
connexion.commit()



cursor.execute("SELECT * FROM user")
print(cursor.fetchall())