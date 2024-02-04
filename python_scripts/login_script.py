import time 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome()


driver.get("https://upvote.biz/auth/login")
time.sleep(5)

username_input = driver.find_element(By.NAME, "email")
password_input = driver.find_element(By.NAME, "password")
username_input.send_keys("nntycobluntzblzyco@cazlp.com")
password_input.send_keys("Password123")

password_input.send_keys(Keys.RETURN)
time.sleep(5)

driver.quit()