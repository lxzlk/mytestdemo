import unittest
from selenium import webdriver
from time import sleep
import xlwt
from readexcelnew import style

driver = webdriver.Chrome()
driver.get("http://10.138.23.192:8080/login")
driver.find_element_by_id('username').send_keys('caiwutest')
driver.find_element_by_id('password').send_keys('123456')
driver.find_element_by_id('btnLogin').click()
sleep(5)

driver.get_screenshot_as_file(
    "E:\pic\\login_success.png"
)
#加权限限后，增加面板
driver.find_element_by_partial_link_text('黑名单').click()
driver.find_element_by_id('commercialRegCert').send_keys('12150523460701166R')
driver.find_element_by_id('btnSearch').click()
sleep(3)
driver.get_screenshot_as_file("E:\pic\\search1.png")
sleep(2)
driver.find_element_by_id('commercialRegCert').clear()
file = xlwt.Workbook('G:\\result.xls')
tt = file.add_sheet('test')
with open('G:\工作资料\黑名单项目\脚本\custname快捷通.txt', encoding='utf-8') as f:
    #for i in f.readlines():
    for (num, value) in enumerate(f):
     #   print(i.strip())
        driver.find_element_by_id('custName').send_keys(value.strip())
        driver.find_element_by_id('btnSearch').click()
        tt.write(num, 0, value, style)
        sleep(7)
        targets_url_1 = driver.find_element_by_id('table_details').find_element_by_xpath('//*[@id="table_details"]/tbody/tr/td[4]').text
        tt.write(num, 1, targets_url_1)
        print(targets_url_1)
        driver.find_element_by_id('custName').clear()
#text1 = driver.find_elements_by_xpath("//*[@id='table_details']")
#print(text1)
file.save('G:\工作资料\黑名单项目\脚本\\result.xls')
print('测试完毕！')

driver.quit()


