from time import sleep
import xlwt
from sqsylogin import driver


file = xlwt.Workbook('G:\\sunyibiao_micro_年.xls')

driver.find_element_by_xpath('/html/body/div/div[2]/div[1]/div[3]/button').click()
sleep(2)
driver.find_element_by_xpath('/html/body/div/div[3]/div[4]')
#季　１１列　月１３列　年　７列
#driver.find_element_by_xpath('/html/body/div/div[3]/div[3]/button[2]').click()
#年
driver.find_element_by_xpath('/html/body/div/div[3]/div[4]/button[3]').click()
#选一级小微（财务公司）
driver.find_element_by_xpath('/html/body/div/div[3]/div[3]/div[2]/button').click()
driver.find_element_by_xpath('/html/body/div/div[3]/div[3]/div[2]/div/ul/li[2]/a/span[1]').click()
sleep(1)
#选二级小微
driver.find_element_by_xpath('/html/body/div/div[3]/div[3]/div[3]/button/span[1]').click()
microcomp = driver.find_element_by_xpath('/html/body/div/div[3]/div[3]/div[3]/div/ul')
lis = microcomp.find_elements_by_css_selector('li')
print(lis)
sleep(1)
for i in lis:
    num = int(i.get_attribute('data-original-index'))  #获得data-original-index属性值
    print(num)
    print(i.text)
    i.click()
    sleep(2)
    driver.find_element_by_xpath('/html/body/div/div[3]/div[3]/div[3]/button/span[1]').click()
    tt = file.add_sheet(i.text)
    sleep(2)
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
    sleep(2)


file.save('G:\\sunyibiao_micro_年.xls')
driver.close()

#爬table表数据
# table = driver.find_element_by_class_name('fixed-table-body').find_element_by_xpath('//*[@id="losstable"]/tbody')
# table_rows = table.find_elements_by_tag_name('tr')
# table_cols = table.find_elements_by_tag_name('td')
# print('table_rows:', len(table_rows))
# print('table_cols:', len(table_cols))
# for table_num in range(1, len(table_rows)):
#     for table_num1 in range(0, 7):
#         table_text = table_rows[table_num].find_elements_by_tag_name('td')[table_num1].text
#         tt.write(table_num, table_num1, table_text)
#         print(table_text)
#
# sleep(3)