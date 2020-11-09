from selenium.webdriver.common.by import By

class pagina_Item():
    def __init__(self, driver):
        self.driver = driver
        self.resultado_esperado = (By.CLASS_NAME, 'heading-counter')

    def obtener_Texto(self):
        return self.driver.find_element(*self.resultado_esperado).text


