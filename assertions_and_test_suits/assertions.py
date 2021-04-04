import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

class AssertionsTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path='/usr/bin/chromedriver')     
        driver = cls.driver
        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.get('http://demo-store.seleniumacademy.com/')

    def test_search_field(self):
        self.assertTrue(self.is_element_present(By.NAME, 'q'))

    def test_language_option(self):
        self.assertTrue(self.is_element_present(By.ID, 'select_language'))

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by = how, value = what)
        except NoSuchElementException as variable:
            return False
        return True 


if __name__ == '__main__':
    unittest.main(verbosity = 2)
