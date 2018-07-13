from selenium import webdriver
from time import sleep
import xlwt
from sqsylogin import driver

file = xlwt.Workbook('G:\\shiqiansuanying.xls')
tt = file.add_sheet('test')

custnumname = driver.find_element_by_xpath('/html/body/div/div[1]/div[2]/div[1]').text
print(custnumname)
tt.write(0, 0, custnumname)
custnum = driver.find_element_by_id('khs').text
tt.write(0, 1, custnum)
xqhtjename = driver.find_element_by_xpath('/html/body/div/div[1]/div[3]/div[1]').text
xqhtje = driver.find_element_by_id('xqhtje').text
tt.write(1, 0, xqhtjename)
tt.write(1, 1, xqhtje)
driver.find_element_by_xpath('/html/body/div/div[2]/div[1]/div[1]/div[1]/div[2]/button[2]').click()
sleep(3)
driver.find_element_by_xpath('//*[@id="chart4"]/div[5]').click()
#print(aa)
#print(filter(str.isdigit, aa))



file.save('G:\\shiqiansuanying.xls')

