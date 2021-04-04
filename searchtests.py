import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver



class HelloWorld(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path='/usr/bin/chromedriver')     
        driver = cls.driver
        driver.get('http://demo-store.seleniumacademy.com/')
        driver.maximize_window()


    def test_search_text_field(self):
        search_field = self.driver.find_element_by_id('search')

    
    def test_search_text_field_by_name(self):
        search_field = self.driver.find_element_by_name('q')
    
    def test_search_text_field_class_name(self):
        search_field = self.driver.find_element_by_class_name('input-text')

    # if button exists
    def test_search_button_enabled(self):
        button = self.driver.find_element_by_class_name('button')
    # list
    def test_count_of_promo_banner_images(self):
        banner_list = self.driver.find_element_by_class_name('promos')
        banners = banner_list.find_elements_by_tag_name('img')
        self.assertEqual(3, len(banners))
    
    # xpath -> there aren't name, class or id
    def test_vip_promo(self):
        vip_promo = self.driver.find_element_by_xpath('//*[@id="top"]/body/div/div[2]/div[2]/div/div/div[2]/div[1]/ul/li[2]/a/img')
    
    def test_shopping_cart(self):
        shopping_cart_icon = self.driver.find_element_by_css_selector('div.header-minicart span.icon')


    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity = 2, testRunner = HTMLTestRunner(output = 'reportes', report_name = 'hello-world-report'))
