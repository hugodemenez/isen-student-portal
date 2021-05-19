import sqlite3

import os

path = "database/database.db"
if os.path.isfile(path):
    connexion = sqlite3.connect(path)
    cursor = connexion.cursor()
    #Add user to user table :
    users=[{
    'username' : 'p63058',
    'password' : 'vYYuQxIx',
    'email' : 'guillaume.gulli@isen.yncrea.fr'
    },
    {
    'username' : 'p64059',
    'password' : 'ny5mJb8z',
    'email' : 'hugo.demenez@isen.yncrea.fr'
    },
    {
    'username' : 'admin',
    'password' : 'password',
    'email' : ''
    }]

    for user in users:
        parametres = (user['username'],user['password'],user['email'])
        command = "INSERT OR REPLACE INTO user VALUES (?,?,?)"
        cursor.execute(command,parametres)
        connexion.commit()
    cursor.execute("SELECT * FROM user")
    print(cursor.fetchall())

else:
    print("Database does not exist")