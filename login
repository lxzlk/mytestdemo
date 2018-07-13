import unittest
from selenium import webdriver
from time import sleep


driver = webdriver.Chrome()
driver.get("http://10.138.23.192:8080/login")
driver.find_element_by_id('username').send_keys('fawutest')
driver.find_element_by_id('password').send_keys('123456')
driver.find_element_by_id('btnLogin').click()
sleep(5)
driver.get_screenshot_as_file(
    "E:\pic\\login_success.png"
)
driver.find_element_by_id('commercialRegCert').send_keys('12150523460701166R')
driver.find_element_by_id('btnSearch').click()
sleep(3)
driver.get_screenshot_as_file("E:\pic\\search1.png")
sleep(2)
driver.find_element_by_id('commercialRegCert').clear()
driver.find_element_by_id('custName').send_keys('江苏雅百特科技股份有限公司')
driver.find_element_by_id('btnSearch').click()
sleep(5)
targets_url_1 = driver.find_element_by_id('table_details').find_element_by_xpath('//*[@id="table_details"]/tbody/tr/td[4]').text
print(targets_url_1)
#text1 = driver.find_elements_by_xpath("//*[@id='table_details']")
#print(text1)
print('测试完毕！')

driver.quit()