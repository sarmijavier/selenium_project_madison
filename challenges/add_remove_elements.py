import unittest
from selenium import webdriver
from time import sleep

class NavigationTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path='/usr/bin/chromedriver')     
        driver = self.driver
        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.get('https://the-internet.herokuapp.com/')
        driver.find_element_by_link_text('Add/Remove Elements').click()


    def test_add_remove(self):
        driver = self.driver

        elements_added = int(input('How many elements will you add?: '))
        elements_removed = int(input('How many elements will you removed?: '))
        total_elements = elements_added - elements_removed

        add_button = driver.find_element_by_xpath('/html/body/div[2]/div/div/button')

        sleep(3)

        for i in range(elements_added):
            add_button.click()
        
        for i in range(elements_removed):
            try:
                delete_button = driver.find_elements_by_xpath('/html/body/div[2]/div/div/div/button[1]')
                delete_button.click()
            except:
                print('You\'re trying to delet more elements than exist')
                break
        
        if total_elements > 0:
            print(f'there are {total_elements} elements on screen')
        
        else:
            print('There are 0 elements on the screen')
        
        sleep(3)

        
    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
	unittest.main(verbosity = 2)