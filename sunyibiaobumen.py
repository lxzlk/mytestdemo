from time import sleep
import xlwt
from sqsylogin import driver
from readexcelnew import style

file = xlwt.Workbook('G:\\sunyibiaobumen.xls')
tt = file.add_sheet('损益表二级小微')
sleep(2)
driver.find_element_by_xpath('/html/body/div/div[3]/div[1]/div[3]/button/div').click()
sleep(2)
#财务公司
comp_cw = driver.find_element_by_xpath('/html/body/div/div[3]/div[2]/div[2]/button/span[1]').text
driver.find_element_by_xpath('/html/body/div/div[3]/div[2]/div[3]/button/span[1]').click()
microcomp_cw = driver.find_element_by_xpath('/html/body/div/div[3]/div[2]/div[3]/div/ul').text
print(comp_cw)
print(microcomp_cw)
sleep(3)
#产业金融
driver.find_element_by_xpath('/html/body/div/div[3]/div[2]/div[2]/button/span[1]').click()
driver.find_element_by_xpath('/html/body/div/div[3]/div[2]/div[2]/div/ul/li[2]/a/span[1]').click()
sleep(2)
comp_cy = driver.find_element_by_xpath('/html/body/div/div[3]/div[2]/div[2]/button/span[1]').text
sleep(2)
driver.find_element_by_xpath('/html/body/div/div[3]/div[2]/div[3]/button/span[1]').click()
microcomp_cy = driver.find_element_by_xpath('/html/body/div/div[3]/div[2]/div[3]/div/ul').text
print(comp_cy)
print(microcomp_cy)
#海尔云贷
driver.find_element_by_xpath('/html/body/div/div[3]/div[2]/div[2]/button/span[1]').click()
driver.find_element_by_xpath('/html/body/div/div[3]/div[2]/div[2]/div/ul/li[3]/a/span[1]').click()
sleep(2)
comp_yd = driver.find_element_by_xpath('/html/body/div/div[3]/div[2]/div[2]/button/span[1]').text
sleep(2)
driver.find_element_by_xpath('/html/body/div/div[3]/div[2]/div[3]/button/span[1]').click()
microcomp_yd = driver.find_element_by_xpath('/html/body/div/div[3]/div[2]/div[3]/div/ul').text
print(comp_yd)
print(microcomp_yd)
#消费金融
driver.find_element_by_xpath('/html/body/div/div[3]/div[2]/div[2]/button/span[1]').click()
driver.find_element_by_xpath('/html/body/div/div[3]/div[2]/div[2]/div/ul/li[6]/a/span[1]').click()
sleep(2)
comp_xj = driver.find_element_by_xpath('/html/body/div/div[3]/div[2]/div[2]/button/span[1]').text
sleep(2)
driver.find_element_by_xpath('/html/body/div/div[3]/div[2]/div[3]/button/span[1]').click()
microcomp_xj = driver.find_element_by_xpath('/html/body/div/div[3]/div[2]/div[3]/div/ul').text
print(comp_xj)
print(microcomp_xj)
#海尔保理
driver.find_element_by_xpath('/html/body/div/div[3]/div[2]/div[2]/button/span[1]').click()
driver.find_element_by_xpath('/html/body/div/div[3]/div[2]/div[2]/div/ul/li[4]/a/span[1]').click()
sleep(2)
comp_bl = driver.find_element_by_xpath('/html/body/div/div[3]/div[2]/div[2]/button/span[1]').text
sleep(2)
driver.find_element_by_xpath('/html/body/div/div[3]/div[2]/div[3]/button/span[1]').click()
microcomp_bl = driver.find_element_by_xpath('/html/body/div/div[3]/div[2]/div[3]/div/ul').text
print(comp_bl)
print(microcomp_bl)
tt.write(0, 0, comp_cw)
tt.write(1, 0, microcomp_cw, style)
tt.write(0, 1, comp_cy)
tt.write(1, 1, microcomp_cy, style)
tt.write(0, 2, comp_yd)
tt.write(1, 2, microcomp_yd, style)
tt.write(0, 3, comp_xj)
tt.write(1, 3, microcomp_xj, style)
tt.write(0, 4, comp_bl)
tt.write(1, 4, microcomp_bl, style)
file.save('G:\\sunyibiaobumen.xls')

driver.close()