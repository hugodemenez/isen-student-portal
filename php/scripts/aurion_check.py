import sys
from webscraping import scraping

print("true")
username = sys.argv[1]
password = sys.argv[2]


if scraping().check_connection(username,password):
    print("true")
else :
    print("false")

    