import unittest
from selenium import webdriver
from time import sleep


class SearchDDT(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path='/usr/bin/chromedriver')     
        driver = self.driver
        driver.get('https://www.mercadolibre.com')
        driver.maximize_window()



    def test_search_ps4(self):
        driver = self.driver

        country = driver.find_element_by_id('CO')
        country.click()

        search_field = driver.find_element_by_xpath('/html/body/header/div/form/input')
        search_field.click()
        search_field.clear()
        search_field.send_keys('playstation 4')
        search_field.submit()
        sleep(3)

        location = driver.find_element_by_class_name('ui-search-filter-name')
        location.click()
        sleep(3)

        condition = driver.find_element_by_class_name('ui-search-filter-name')
        condition.click()
        sleep(3)

        order_menu = driver.find_element_by_class_name('andes-dropdown__trigger')
        order_menu.click()
        higher_price = driver.find_element_by_css_selector('#root-app > div > div > section > div.ui-search-view-options__container > div > div > div.ui-search-view-options__group > div.ui-search-sort-filter > div > div > div > ul > li:nth-child(3) > a > div > div')
        higher_price.click()
        sleep(3)

        articles = []
        prices = []

        for i in range(3):
            articles_name = driver.find_element_by_xpath(f'//*[@id="root-app"]/div/div/section/ol/li[{i + 1}]/div/div/div[2]/div[1]/a/h2').text
            articles.append(articles_name)
        
        for i in range(3):
            article_price = driver.find_element_by_xpath(f'//*[@id="root-app"]/div/div/section/ol/li[{i + 1}]/div/div/div[2]/div[2]/div[1]/div[1]/div/div/span[1]/span[2]').text
            prices.append(article_price)
        
        print(articles, prices)

 
    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
	unittest.main(verbosity = 2)