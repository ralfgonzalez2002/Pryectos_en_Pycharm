from selenium.webdriver.common.by import By

class Products:
    def __init__(self, driver):
        self.driver = driver
        self.ingress_quantity = (By.NAME, 'qty')
        self.btn_plus = (By.XPATH, '//*[@id="quantity_wanted_p"]/a[2]/span')

    def set_quantity(self, quantity):
        self.driver.find_element(*self.ingress_quantity).clear()
        self.driver.find_element(*self.ingress_quantity).send_keys(quantity)

    def click_plus(self, quantity):
        for i in range(quantity):
            self.driver.find_element(*self.btn_plus).click()

    def return_quantity(self):
        return self.driver.find_element(*self.ingress_quantity).get_attribute('value')




