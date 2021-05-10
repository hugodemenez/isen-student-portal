from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from time import sleep
import requests
import xml.etree.ElementTree as ET

options = Options()
options.headless = True
options.binary_location = r"C:\Program Files\Mozilla Firefox\firefox.exe"
driver = webdriver.Firefox(options=options, executable_path="geckodriver.exe")
driver.get('https://aurion.junia.com/faces/Login.xhtml')

inputElement = driver.find_element_by_id("username")
inputElement.send_keys('p64059')
inputElement = driver.find_element_by_id("password")
inputElement.send_keys('ny5mJb8z')

inputElement.submit() 
requete= requests.post('https://aurion.junia.com/faces/Planning.xhtml')

print(requete.text)

