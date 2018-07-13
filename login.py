import unittest
from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get("http://10.138.23.192:8080/login")
driver.find_element_by_id('username').send_keys('01484175')
driver.find_element_by_id('password').send_keys('123456')
driver.find_element_by_id('btnLogin').click()
sleep(4)
driver.find_element_by_partial_link_text('客户评级').click()
sleep(4)