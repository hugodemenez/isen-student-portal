from seleniumwire import webdriver  # Import from seleniumwire
from selenium.webdriver.firefox.options import Options
from time import sleep
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
sleep(10)
inputElement =driver.find_element_by_link_text("Mon Planning")
inputElement.click() 


cookies=driver.get_cookies()
cookie = cookies[0]['value']


# Access requests via the `requests` attribute
for request in driver.requests:
    if request.response:
        response = request.response.body



print(response)