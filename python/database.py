import sqlite3

connexion = sqlite3.connect("python/sqlite.db")

cursor = connexion.cursor()




#Add user to user table :
cursor.execute("""INSERT INTO user VALUES ("hugodemenez","mdp","hugo")""")


cursor.execute("SELECT * FROM user")

print(cursor.fetchall())