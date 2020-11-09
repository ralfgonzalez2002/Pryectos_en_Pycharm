from selenium.webdriver.common.by import By

class pagina_Inicio():
    def __init__(self, driver):
        self.driver = driver
        self.txt_bucador = (By.ID, 'search_query_top')
        self.btn_bucar = (By.NAME, 'submit_search')

    def ingresar_item(self, item):
        self.driver.find_element(*self.txt_bucador).send_keys(item)

    def click_buscar(self):
        self.driver.find_element(*self.btn_bucar).click()

