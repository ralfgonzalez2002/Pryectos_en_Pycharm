import unittest
from selenium import webdriver
import time


class SearchCases(unittest.TestCase):
    def test_search_find_dresses (self):
        driver = webdriver.Chrome('../drivers/chromedriver.exe')
        driver.get('http://automationpractice.com/index.php')
        driver.find_element_by_name('search_query').send_keys('dress')
        driver.find_element_by_name('submit_search').click()
        time.sleep(2)
        self.assertTrue('DRESS' in driver.find_element_by_xpath('//*[@id="center_column"]/h1').text)
        driver.close()
        driver.quit()

    def test_search_no_elements (self):
        driver = webdriver.Chrome('chromedriver.exe')
        driver.get('http://automationpractice.com/index.php')
        driver.find_element_by_name('search_query').send_keys('hola')
        driver.find_element_by_name('submit_search').click()
        time.sleep(2)
        self.assertEqual(driver.find_element_by_xpath('//*[@id="center_column"]/p').text, 'No results were found for your search "hola"')
        driver.close()
        driver.quit()

    def test_search_find_tshirts (self):
        driver = webdriver.Chrome('chromedriver.exe')
        driver.get('http://automationpractice.com/index.php')
        driver.find_element_by_name('search_query').send_keys('t-shirt')
        driver.find_element_by_name('submit_search').click()
        time.sleep(2)
        self.assertTrue('T-SHIRT' in driver.find_element_by_xpath('//*[@id="center_column"]/h1').text)
        driver.close()
        driver.quit()





if __name__ == '__main__':
    unittest.main()