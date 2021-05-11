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
headers = {
"Host": "aurion.junia.com",
"Connection": "keep-alive",
"Content-Length": "584",
"Accept": "application/xml, text/xml, */*; q=0.01",
"X-Requested-With": "XMLHttpRequest",
"Faces-Request": "partial/ajax",
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36",
"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
"Sec-GPC": "1",
"Origin": "https://aurion.junia.com",
"Sec-Fetch-Site": "same-origin",
"Sec-Fetch-Mode": "cors",
"Sec-Fetch-Dest": "empty",
"Referer": "https://aurion.junia.com/faces/Planning.xhtml",
"Accept-Encoding": "gzip, deflate, br",
"Accept-Language": "fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7",
"Cookie": "JSESSIONID=55A38E3494946FEDB6E33829198A1F52",
}

reponse = requests.post('https://aurion.junia.com/faces/Planning.xhtml',headers=headers)
print(reponse.text)