from selenium import webdriver
import unittest
import time

#tc = unittest.TestCase ('__init__')
driver = webdriver.Chrome('chromedriver.exe')
driver.get ('http://automationpractice.com/index.php')
search_box = driver.find_element_by_id('search_query_top')
search_box.send_keys('Hola Mundo')
search_box_button = driver.find_element_by_name('submit_search')
search_box_button.click()
time.sleep(5)
results_label = driver.find_element_by_xpath('//*[@id="center_column"]/p')
#tc.assertEqual('No results were found for your search "Hola Mundo"', results_label.text)
time.sleep(5)
woman_link = driver.find_element_by_link_text('Women')
woman_link.click()
time.sleep(5)
driver.close()
driver.quit()
 
