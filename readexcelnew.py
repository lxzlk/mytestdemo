import xlwt
import unittest


style = xlwt.XFStyle()  # 初始化样式
alignment = xlwt.Alignment()
alignment.wrap = xlwt.Alignment.WRAP_AT_RIGHT # 自动换行
style.alignment = alignment
if __name__ == '__main__':
    file = xlwt.Workbook('G:\\result1.xls')
    tt = file.add_sheet('test')
    with open('G:\工作资料\黑名单项目\脚本\custname1.txt', encoding='utf-8') as f:
        #for i in f.readlines():
        for (num1, value1) in enumerate(f):
            #print(i.strip())
            value1.strip()
            tt.write(num1, 0, value1, style)
            print(num1, value1)
    file.save('G:\工作资料\黑名单项目\脚本\\result1.xls')


