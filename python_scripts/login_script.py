import time 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select


def run_job(link_input, comment_input, email="geteceh687@bitofee.com", password=""):
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')
    driver = webdriver.Chrome(options=options)

    driver.get("https://upvote.biz/auth/login")
    time.sleep(5)

    username_input = driver.find_element(By.NAME, "email")
    password_input = driver.find_element(By.NAME, "password")
    time.sleep(2)
    username_input.send_keys(email)
    password_input.send_keys(password)
    time.sleep(2)
    password_input.send_keys(Keys.RETURN)
    time.sleep(10)

    category_id = Select(driver.find_element(By.NAME, "category_id"))
    time.sleep(1)
    category_id.select_by_value("29")
    time.sleep(1)
    service_id = Select(driver.find_element(By.NAME, "service_id"))
    time.sleep(1)
    service_id.select_by_value("5")
    time.sleep(1)
    link = driver.find_element(By.NAME, "link")
    link.send_keys(link_input)
    time.sleep(1)
    comments = driver.find_element(By.NAME, "comments")
    comments.send_keys(comment_input)
    time.sleep(1)

    agree = driver.find_element(By.NAME, "agree")
    agree.click()
    time.sleep(5)

    place_order = driver.find_element(By.CLASS_NAME, "btn-primary")
    place_order.click()
    time.sleep(10)

    driver.quit()