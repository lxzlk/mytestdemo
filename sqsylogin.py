from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get("http://10.138.25.74:8100/html/login.html")
sleep(2)
driver.find_element_by_name('username').send_keys('test')
driver.find_element_by_id('loginpwd').send_keys('123Abc')
driver.find_element_by_xpath('//*[@id="login"]/button').click()
sleep(4)