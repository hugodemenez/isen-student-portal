#!/usr/bin/env python3.9
import sys

try:
    from webscraping import scraping
except Exception as e:
    print(e)

username = sys.argv[1]
password = sys.argv[2]

try:
    if scraping().check_connection(username,password):
        print("true")
    else :
        print("false")
except Exception as e:
    print(e)