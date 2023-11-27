from django.test import TestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

#Selenium test cases
class RegisterLogan(TestCase):
    def test_register_user(self):
        driver = webdriver.Chrome()
        driver.get("http://127.0.0.1:8000/logout/")
        driver.implicitly_wait(0.5)
        driver.get("http://127.0.0.1:8000/")
        driver.implicitly_wait(0.5)
        driver.set_window_size(1300, 900)
        driver.find_element(by=By.LINK_TEXT, value="Account").click()
        driver.implicitly_wait(0.5)
        driver.find_element(by=By.LINK_TEXT, value="Register").click()
        driver.implicitly_wait(0.5)
        driver.find_element(by=By.NAME, value="username").send_keys("logan")
        driver.find_element(by=By.NAME, value="email").send_keys("lo@gmail.com")
        driver.find_element(by=By.NAME, value="password1").send_keys("happypass1")
        driver.find_element(by=By.NAME, value="password2").send_keys("happypass1")
        driver.find_element(by=By.NAME, value="Create User").click()
        driver.implicitly_wait(0.5)
        driver.find_element(by=By.NAME, value="username").send_keys("logan")
        driver.find_element(by=By.NAME, value="password").send_keys("happypass1")
        driver.find_element(by=By.CSS_SELECTOR, value=".btn-primary").click()

class CreateDeleteClip(TestCase):
    def test_clip_usage(self):
        driver = webdriver.Chrome()
        driver.get("http://127.0.0.1:8000/logout/")
        driver.implicitly_wait(0.5)
        driver.get("http://127.0.0.1:8000/login/")
        driver.implicitly_wait(0.5)
        driver.find_element(by=By.NAME, value="username").send_keys("bradyn")
        driver.find_element(by=By.NAME, value="password").send_keys("happypass1")
        driver.find_element(by=By.CSS_SELECTOR, value=".btn-primary").click()
        driver.implicitly_wait(0.5)
        driver.set_window_size(1300, 900)
        driver.find_element(by=By.LINK_TEXT, value="Your Clips").click()
        driver.implicitly_wait(0.5)
        driver.find_element(by=By.CSS_SELECTOR, value=".btn-primary").click()
        driver.find_element(by=By.NAME, value="title").send_keys("Example Clip")
        Select(driver.find_element(by=By.NAME, value="game")).select_by_visible_text("Apex")
        driver.find_element(by=By.NAME, value="description").send_keys("Simple Description")
        driver.find_element(by=By.NAME, value="Submit").click()
        driver.implicitly_wait(0.5)
        driver.find_element(by=By.CSS_SELECTOR, value=".card:nth-child(5) .btn").click()
        driver.find_element(by=By.CSS_SELECTOR, value=".btn-secondary").click()
        driver.find_element(by=By.NAME, value="submit").click()



        


        
        

        



