import sys
from webscraping import scraping

username = sys.argv[1]
password = sys.argv[2]


if scraping().check_connection(username,password):
    print("true")
else :
    print("false")

    