from selenium.webdriver.common.by import By

class PageIndex():
    def __init__(self, driver):
        #self.query_search = 'search_query'
        #self.search_button = 'submit_search'
        self.query_search = (By.NAME, 'search_query')
        self.search_button = (By.NAME, 'submit_search')
        self.driver = driver

    def search(self, item):
        #self.driver.find_element_by_name(self.query_search).send_keys(item)
        #self.driver.find_element_by_name(self.search_button).click()
        self.driver.find_element(*self.query_search).send_keys(item)
        self.driver.find_element(*self.search_button).click()




