from selenium.webdriver.common.by import By

class PageItem:
    def __init__(self, driver):
        self.no_result_banner = (By.XPATH, '//*[@id="center_column"]/p')
        self.title_banner = (By.XPATH, '//*[@id="center_column"]/h1')
        self.orange_color = (By.XPATH, '//*[@id="color_1"]')
        self.driver = driver

    def return_no_element_text(self):
        return self.driver.find_element(*self.no_result_banner).text

    def return_section_title(self):
        return self.driver.find_element(*self.title_banner).text

    def select_orange_color(self):
        self.driver.find_element(*self.orange_color).click()


