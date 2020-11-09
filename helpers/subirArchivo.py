#TC_0002
#Descripción: Se da de alta un documento de tipo GENERAL con el Rol: ADMIN, en la ubicación DOCUMENTOS.

from selenium import webdriver
from selenium.webdriver.support.ui import Select
import os

picture = ("C:\image.jpg")
chrome_options = webdriver.ChromeOptions()
driver = webdriver.Chrome('Chromedriver.exe')
driver.maximize_window()
chrome_options.add_argument("--incognito")

driver.get('https://portaldistribuidores-dev.abinbev-las.com/login')
driver.implicitly_wait(20)

#inicio de sesión
usuario = driver.find_element_by_name('UserName')
usuario.click()
usuario.send_keys('lyromano@quilmes.com.ar')

contraseña = driver.find_element_by_name('Password')
contraseña.click()
contraseña.send_keys('Quilmes2020')

btn_login = driver.find_element_by_id('submitButton')
btn_login.click()
driver.implicitly_wait(20)

#ir a documentos
documentos = driver.find_element_by_xpath('/html[1]/body[1]/app-root[1]/block-ui[1]/app-pages[1]/app-default-layout[1]/div[2]/div[1]/app-navbar[1]/div[1]/ul[1]/li[5]/a[1]')
documentos.click()
driver.implicitly_wait(20)

#alta de una carpeta para generalW
btn_crearnuevo = driver.find_element_by_xpath('/html[1]/body[1]/app-root[1]/block-ui[1]/app-pages[1]/app-default-layout[1]/div[2]/div[2]/main[1]/app-list[1]/div[1]/div[1]/div[1]/div[2]/button[1]')
btn_crearnuevo.click()

btn_new_documento = driver.find_element_by_xpath('/html[1]/body[1]/app-root[1]/block-ui[1]/app-pages[1]/app-default-layout[1]/div[2]/div[2]/main[1]/app-list[1]/div[1]/div[1]/div[1]/div[2]/div[1]/ul[1]/li[1]/a[1]')
btn_new_documento.click()

input_name = driver.find_element_by_xpath("//input[@placeholder='Nombre']")
input_name.send_keys('TC_#0002 - CARPETA PARA GENERAL')

input_description = driver.find_element_by_name('description')
input_description.send_keys('TC_#0002 - DESCRIPCIÓN')

carpeta = Select(driver.find_element_by_name('contenido'))
carpeta.select_by_visible_text('|- TC_#0001 - CARPETA PARA GENERAL')

#driver.find_element_by_xpath('//*[@id="body"]/modal-container/div/div/app-edit/form/div[1]/div/div[3]/div/div[1]/label').send_keys("C:\estatua.jpg")

driver.find_element_by_xpath('//*[@id="body"]/modal-container/div/div/app-edit/form/div[1]/div/div[3]/div/div[1]/label').send_keys(os.getcwd()+"C:/estatua.jpg")

#driver.find_element_by_id("id-of-uploadfile-element").send_keys("file-path")
#driver.find_element_by_id("submit").click()

tipoContenido = Select(driver.find_element_by_name('contentTypeCode'))
tipoContenido.select_by_index('1')

guardar = driver.find_element_by_xpath("//button[@class='btn btn-primary']")
guardar.click()