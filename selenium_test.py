import os
import time
import unittest
import unittest.mock

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import tinydb

from db import helpers

YOUFACE_URL = "http://localhost:5000"


class TestLoginPage(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass


    # def test_login(self):
    #     driver = webdriver.Chrome()

    #     # 1. request home page
    #     driver.get(YOUFACE_URL)

    #     #
    #     # Test invalid login
    #     #

    #     # 2. enter username and password
    #     try:
    #         username_box = driver.find_element(By.NAME, "username")
    #     except NoSuchElementException:
    #         self.fail("Failed to find the username input box.")
    #     username_box.send_keys("invalid")

    #     try:
    #         password_box = driver.find_element(By.NAME, "password")
    #     except NoSuchElementException:
    #         self.fail("Failed to find the password input box.")
    #     password_box.send_keys("invalid")

    #     # 3. click login button
    #     try:
    #         login_btn = driver.find_element(By.CLASS_NAME, "btn-primary")
    #     except NoSuchElementException:
    #         self.fail("Failed to find the login button.")
    #     login_btn.click()

    #     # test login worked
    #     self.assertIn("loginscreen", driver.current_url)


    #     #
    #     # test valid login
    #     #

    #     try:
    #         username_box = driver.find_element(By.NAME, "username")
    #     except NoSuchElementException:
    #         self.fail("Failed to find the username input box.")
    #     username_box.send_keys(self.username)
    #     try:
    #         password_box = driver.find_element(By.NAME, "password")
    #     except NoSuchElementException:
    #         self.fail("Failed to find the password input box.")
    #     password_box.send_keys(self.username)
    #     try:
    #         login_btn = driver.find_element(By.CLASS_NAME, "btn-primary")
    #     except NoSuchElementException:
    #         self.fail("Failed to find the login button.")
    #     login_btn.click()
    #     self.assertNotIn("loginscreen", driver.current_url)

    #     driver.close()

    def test_create_user(self):
        driver = webdriver.Chrome()
        #
        # test empty username and password
        #
        "As a user, if I type in a blank username and password, I should not be able to create a user"
        driver.get(YOUFACE_URL)

        time.sleep(3)

        # try:
        #     create_btn = driver.find_element(By.CLASS_NAME, "btn-success")
        # except NoSuchElementException:
        #     self.fail("Failed to find the create button.")
        # create_btn.click()

        self.assertIn("loginscreen", driver.current_url)

        driver.close()

    #def test_delete_user(self):
        #pass

if __name__ == "__main__":
    unittest.main()
