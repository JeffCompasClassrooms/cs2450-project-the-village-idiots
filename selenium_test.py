import os
import time
import unittest
import unittest.mock

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


YOUFACE_URL = "http://localhost:5000"


class TestLoginPage(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass


    def test_create_user(self):
        chrome_options = Options()
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--headless")
        timestamp = str(int(time.time()))
        user_data_dir = f"--user-data-dir=/tmp/chrome-user-data-{timestamp}"
        chrome_options.add_argument(user_data_dir)

        driver = webdriver.Chrome(options=chrome_options)
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


if __name__ == "__main__":
    unittest.main()
