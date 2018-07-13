from selenium import webdriver
from time import sleep
from login import driver
from selenium.webdriver.support.ui import Select
sleep(2)
driver.find_element_by_xpath('//*[@id="main_left"]/ul/li[8]').click()
sleep(2)
driver.find_element_by_partial_link_text('进入评级').click()
sleep(5)
driver.find_element_by_id('compName').click()
sleep(2)
Select(driver.find_element_by_id("compName")).select_by_value('0K00')
driver.find_element_by_id('custCode').send_keys('深圳前海未来教育科技有限公司')
sleep(2)
driver.find_element_by_xpath('//*[@id="mainContentDiv"]/div[1]/div/ul/li').click()
driver.find_element_by_id('sub1').click()
sleep(3)
driver.find_element_by_id('sub3').click()
driver.find_element_by_xpath('/html/body/div[1]/div/table/tbody/tr[2]/td[2]/div/table/tbody/tr[3]/td/div/button[1]').click()
sleep(2)
driver.find_element_by_xpath('//*[@id="table_details"]/tbody/tr/td[10]/a[2]').click()
