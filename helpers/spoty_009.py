# -*- coding: utf-8 -*-
import unittest
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import os
import autoit



class SpotyTestCase(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://smallpdf.com/es/word-a-pdf')
        self.driver.maximize_window()
        self.driver.implicitly_wait(15)
        self.wait = WebDriverWait(self.driver, 30)


    def test_ventanas(self):
        fileButton = "//div[@class='sc-1rkezdt-4 cwMDkh']"
        self.wait.until(EC.visibility_of_element_located((By.XPATH, fileButton)))
        time.sleep(3)
        self.driver.find_element(By.XPATH, fileButton).click()
        #basedir = os.path.abspath(os.path.join(__file__, "../.."))
        #print(basedir + "tests/capturas/Temario.docx")
        #autoit.win_wait("[CLASS:#32770;TITLE:Abrir]", 5)
        #time.sleep(3)
        #autoit.control_click("[CLASS:#32770;TITLE:Abrir]", "ToolbarWindow324")
        #autoit.control_send("[CLASS:#32770;TITLE:Abrir]", "UniversalSearchBand1", "TP AlumnosEstadisticas")

        #time.sleep(3)
        autoit.win_wait("[CLASS:#32770;TITLE:Abrir]", 5)
        time.sleep(3)
        autoit.control_send("[CLASS:#32770;TITLE:Abrir]", "Edit1", "REDES_P1_03062020.doc")
        autoit.control_click("[CLASS:#32770;TITLE:Abrir]", "Button1")


        time.sleep(5)





    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
