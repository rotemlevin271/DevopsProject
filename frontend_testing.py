from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep
# starting a webdriver session
driver = webdriver.Chrome(service=Service("C:/Users/rotem/Downloads/chromedriver_win32/chromedriver.exe"))
# navigating to URL with existing id
driver.get('http://127.0.0.1:5001/users/1')
# check if username element showing and print it
element = driver.find_elements(By.ID, "user")
print(element)
just_user_name = element.text
print("User name: " + just_user_name)
sleep(5)
driver.quit()
