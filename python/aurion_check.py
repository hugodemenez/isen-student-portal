import sys
from webscraping import scraping

username = sys.argv[1]
password = sys.argv[2]
email =sys.argv[3]
niveau = sys.argv[4]
specialite = sys.argv[5]

if scraping().check_connection(username,password):
    print("true")
else :
    print("false")

    