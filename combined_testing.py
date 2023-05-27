import requests

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from db_connector import get_user
# Post request to add new user
res = requests.post('http://127.0.0.1:5000/users/10', json={"user_name":"adi"})
if res.ok:
    print(res.json())
else:
    print('user already exists')

# Get request to check if user exists
res2 = requests.get('http://127.0.0.1:5000/users/6')
if res2.ok:
    print(res.json())
    print('data equals the posted data')

# check posted data is stored in DB
user_name = get_user(3)
if user_name == 'rotemmm':
    print('rotemmm is under id number 3')
else:
    print('user already exists')

# starting a webdriver session
driver = webdriver.Chrome(service=Service("C:/Users/rotem/Downloads/chromedriver_win32/chromedriver.exe"))
driver.implicitly_wait(100)
# navigating to URL with existing id
driver.get('http://127.0.0.1:5001/users/get_user_data/2')
# check if user name element showing and print it
element = driver.find_element(By.ID, "user")
print(element)
just_user_name = element.text
print("User name: " + just_user_name)

driver.quit()

