import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

class ExampleFunctionalTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()

    def tearDown(self):
        self.browser.quit()

    #I NEED TO ADD THIS LOGIN FUNCTION SO THAT IT COULD PASS THE TESTS AND WORK AS INTENDED IN QUIZ QUESTION 8
    def login(self):
        self.browser.get("http://localhost:8000/login")
        
        username_field = self.browser.find_element(By.NAME, "username")
        password_field = self.browser.find_element(By.NAME, "password")
        login_button = self.browser.find_element(By.CSS_SELECTOR, "input[type='submit']")

        username_field.send_keys("aleovity")
        password_field.send_keys("aleoaleo")
        login_button.click()

    def test_heading_text_is_correct(self):
        self.login()

        self.browser.get("http://localhost:8000")
        element: WebElement = self.browser.find_element(by=By.TAG_NAME, value="h1")

        self.assertEqual("Mental Health Tracker", element.text)

    def test_page_title_is_correct(self):

        self.login()

        self.browser.get("http://localhost:8000")
        
        self.assertEqual("PBD Mental Health Tracker", self.browser.title)
