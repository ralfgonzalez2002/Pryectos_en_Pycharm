#TC_0002
#Descripción: Se da de alta un documento de tipo GENERAL con el Rol: ADMIN, en la ubicación DOCUMENTOS.

'''from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
#import autoit
import os, sys

picture = ("C:\image.jpg")
chrome_options = webdriver.ChromeOptions()
driver = webdriver.Chrome('Chromedriver.exe')
driver.maximize_window()
#chrome_options.add_argument("--incognito")

driver.get('https://smallpdf.com/es/word-a-pdf')
driver.implicitly_wait(20)
btnAdjuntar =driver.find_element_by_xpath('//*[@id="__cond-22"]/div/div/div/div/div[2]/form/label/div/div[2]/button[1]')
btnAdjuntar.send_keys('C:\\Users\\rgonzalez\\Pictures\\Saved Pictures\\QSinAlcohol.jfif')
driver.implicitly_wait(20)'''

