from time import sleep
import xlwt
from sqsylogin import driver
file = xlwt.Workbook('G:\\sunyibiao_年.xls')
sleep(2)
driver.find_element_by_xpath('/html/body/div/div[2]/div[1]/div[3]/button/div').click()
sleep(2)
#季　１１列　月１３列　年　７列
driver.find_element_by_xpath('/html/body/div/div[3]/div[4]')
#driver.find_element_by_xpath('/html/body/div/div[3]/div[4]/button[2]').click()
#年
driver.find_element_by_xpath('/html/body/div/div[3]/div[4]/button[3]').click()
sleep(1)
tt0 = file.add_sheet('一级小微')
sleep(1)
table = driver.find_element_by_class_name('fixed-table-body').find_element_by_xpath('//*[@id="losstable"]/tbody')
table_rows = table.find_elements_by_tag_name('tr')
table_cols = table.find_elements_by_tag_name('td')
print('table_rows:', len(table_rows))
print('table_cols:', len(table_cols))
for table_num in range(1, len(table_rows)):
    for table_num1 in range(0, 7):
        table_text = table_rows[table_num].find_elements_by_tag_name('td')[table_num1].text
        tt0.write(table_num, table_num1, table_text)
        print(table_text)

sleep(3)


tt = file.add_sheet('财务公司')
driver.find_element_by_xpath('/html/body/div/div[3]/div[3]/div[2]/button').click()
driver.find_element_by_xpath('/html/body/div/div[3]/div[3]/div[2]/div/ul/li[2]/a/span[1]').click()
sleep(1)
table = driver.find_element_by_class_name('fixed-table-body').find_element_by_xpath('//*[@id="losstable"]/tbody')
table_rows = table.find_elements_by_tag_name('tr')
table_cols = table.find_elements_by_tag_name('td')
print('table_rows:', len(table_rows))
print('table_cols:', len(table_cols))
for table_num in range(1, len(table_rows)):
    for table_num1 in range(0, 7):
        table_text = table_rows[table_num].find_elements_by_tag_name('td')[table_num1].text
        tt.write(table_num, table_num1, table_text)
        print(table_text)

sleep(3)

tt1 = file.add_sheet('产业金融', cell_overwrite_ok=False)
sleep(2)
driver.find_element_by_xpath('/html/body/div/div[3]/div[3]/div[2]/button').click()
sleep(2)
driver.find_element_by_xpath('/html/body/div/div[3]/div[3]/div[2]/div/ul/li[3]/a/span[1]').click()
sleep(4)
#driver.find_element_by_xpath('/html/body/div/div[3]/div[1]/div[3]/button/div').click()
sleep(3)
table = driver.find_element_by_class_name('fixed-table-body').find_element_by_xpath('//*[@id="losstable"]/tbody')
table_rows = table.find_elements_by_tag_name('tr')
table_cols = table.find_elements_by_tag_name('td')
print('table_rows:', len(table_rows))
print('table_cols:', len(table_cols))
for table_num in range(1, len(table_rows)):
    for table_num1 in range(0, 7):
        table_text = table_rows[table_num].find_elements_by_tag_name('td')[table_num1].text
        tt1.write(table_num, table_num1, table_text)
        print(table_text)


sleep(3)

tt2 = file.add_sheet('海尔云贷', cell_overwrite_ok=False)
sleep(2)
driver.find_element_by_xpath('/html/body/div/div[3]/div[3]/div[2]/button').click()
sleep(2)
driver.find_element_by_xpath('/html/body/div/div[3]/div[3]/div[2]/div/ul/li[4]/a/span[1]').click()
sleep(4)
#driver.find_element_by_xpath('/html/body/div/div[3]/div[1]/div[3]/button/div').click()
sleep(3)
table = driver.find_element_by_class_name('fixed-table-body').find_element_by_xpath('//*[@id="losstable"]/tbody')
table_rows = table.find_elements_by_tag_name('tr')
table_cols = table.find_elements_by_tag_name('td')
print('table_rows:', len(table_rows))
print('table_cols:', len(table_cols))
for table_num in range(1, len(table_rows)):
    for table_num1 in range(0, 7):
        table_text = table_rows[table_num].find_elements_by_tag_name('td')[table_num1].text
        tt2.write(table_num, table_num1, table_text)
        print(table_text)


sleep(3)

tt3 = file.add_sheet('金融保理', cell_overwrite_ok=False)
sleep(2)
driver.find_element_by_xpath('/html/body/div/div[3]/div[3]/div[2]/button').click()
sleep(2)
driver.find_element_by_xpath('/html/body/div/div[3]/div[3]/div[2]/div/ul/li[5]/a/span[1]').click()
sleep(4)
#driver.find_element_by_xpath('/html/body/div/div[3]/div[1]/div[3]/button/div').click()
sleep(3)
table = driver.find_element_by_class_name('fixed-table-body').find_element_by_xpath('//*[@id="losstable"]/tbody')
table_rows = table.find_elements_by_tag_name('tr')
table_cols = table.find_elements_by_tag_name('td')
print('table_rows:', len(table_rows))
print('table_cols:', len(table_cols))
for table_num in range(1, len(table_rows)):
    for table_num1 in range(0, 7):
        table_text = table_rows[table_num].find_elements_by_tag_name('td')[table_num1].text
        tt3.write(table_num, table_num1, table_text)
        print(table_text)


sleep(3)

tt4 = file.add_sheet('消费金融', cell_overwrite_ok=False)
sleep(2)
driver.find_element_by_xpath('/html/body/div/div[3]/div[3]/div[2]/button').click()
sleep(2)
driver.find_element_by_xpath('/html/body/div/div[3]/div[3]/div[2]/div/ul/li[6]/a/span[1]').click()
sleep(4)
#driver.find_element_by_xpath('/html/body/div/div[3]/div[1]/div[3]/button/div').click()
sleep(3)
table = driver.find_element_by_class_name('fixed-table-body').find_element_by_xpath('//*[@id="losstable"]/tbody')
table_rows = table.find_elements_by_tag_name('tr')
table_cols = table.find_elements_by_tag_name('td')
print('table_rows:', len(table_rows))
print('table_cols:', len(table_cols))
for table_num in range(1, len(table_rows)):
    for table_num1 in range(0, 7):
        table_text = table_rows[table_num].find_elements_by_tag_name('td')[table_num1].text
        tt4.write(table_num, table_num1, table_text)
        print(table_text)
file.save('G:\\sunyibiao_年.xls')

driver.close()