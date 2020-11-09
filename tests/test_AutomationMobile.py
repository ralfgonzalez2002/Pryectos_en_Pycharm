import unittest
from selenium import webdriver
from pages.page_Inicio import pagina_Inicio
from pages.page_Item import pagina_Item

class pruebas_Mobile(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome('../drivers/chromedriver.exe')
        self.driver.get('http://automationpractice.com/index.php')
        self.driver.implicitly_wait(5)
        self.pagina_Inicio = pagina_Inicio(self.driver)
        self.pagina_Item = pagina_Item(self.driver)

    def test_buscador(self):
        self.pagina_Inicio.ingresar_item('hola')
        self.pagina_Inicio.click_buscar()
        self.assertEqual(self.pagina_Item.obtener_Texto(), '0 results have been found.', 'No deben aparecer elementos para esta búsqueda')

    #@unittest.skip('No ejecutar hasta el 2021')
    def test_elemento_conseguido(self):
        self.pagina_Inicio.ingresar_item('t-shirts')
        self.pagina_Inicio.click_buscar()
        self.assertNotEqual('0 results have been found.', self.pagina_Item.obtener_Texto())

    def tearDown(self):
        self.driver.close()
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()


