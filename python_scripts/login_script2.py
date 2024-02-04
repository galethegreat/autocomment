import time 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome()


driver.get("https://app.reddit.top/login")
time.sleep(2)

username_input = driver.find_element(By.ID, "email")
password_input = driver.find_element(By.ID, "password")
username_input.send_keys("geteceh687@bitofee.com")
password_input.send_keys("Password123")
time.sleep(2)
password_input.send_keys(Keys.RETURN)
time.sleep(5)

driver.quit()