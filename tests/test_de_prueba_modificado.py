import unittest
from selenium import webdriver
import time
from pages.pageIndex import PageIndex
from pages.pageItem import PageItem
from pages.selectProduct import Products
#from selenium.webdriver.chrome.options import Options


class SearchCases(unittest.TestCase):
    def setUp(self):
        #option = Options()
        #option.add_argument("start-maximized")
        #option.add_argument("--headless")
        self.driver = webdriver.Chrome('../drivers/chromedriver.exe')#, chrome_options = option
        self.driver.get('http://automationpractice.com/index.php')
        self.indexPage = PageIndex(self.driver)
        self.itemsPage = PageItem(self.driver)
        self.selectProduct = Products(self.driver)
        self.driver.implicitly_wait(5)

    #Salta este test y no lo ejecuta
    #@unittest.skip("Not needed now")
    def test_search_find_dresses (self):
        self.indexPage.search('dress')
        time.sleep(2)
        self.assertTrue('DRESS' in self.itemsPage.return_section_title())

    # Salta este test y no lo ejecuta
    #@unittest.skip("Not needed now")
    def test_search_no_elements (self):
        self.indexPage.search('hola')
        time.sleep(2)
        self.assertEqual(self.itemsPage.return_no_element_text(), 'No results were found for your search "hola"')

    # Salta este test y no lo ejecuta
    #@unittest.skip("Not needed now")
    def test_search_find_tshirts (self):
        self.indexPage.search('t-shirt')
        time.sleep(2)
        self.assertTrue('T-SHIRT' in self.itemsPage.return_section_title())

    def test_add_to_cart (self):
        self.indexPage.search('t-shirt')
        self.itemsPage.select_orange_color()
        self.selectProduct.set_quantity('25')
        self.selectProduct.click_plus(3)
        self.assertTrue(self.selectProduct.return_quantity() == '28')
        


    def tearDown(self):
        self.driver.close()
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()