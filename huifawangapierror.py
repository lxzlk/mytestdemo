# coding=gbk
import requests
import unittest
import cx_Oracle
import os
from time import sleep
import xlwt
os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'


class TestApi(unittest.TestCase):
    def setUp(self):
        print('start.....')
    #推送接口
    def test_api(self):
        url = 'http://localhost:6001/law/pushContentToHaierFin'
        data = {'content': '{"caipan":[{"casenum":"1","id":"200000000000000000",'
                   '"casetopic":"2",'
                   '"content":"3",'
                   '"court":"4",'
                   '"defendant":"5",'
                   '"furl_casecon":"6",'
                   '"keyid":"7755",'
                   '"money":"8",'
                   '"monitorid":"9",'
                   '"name":"青岛市四方区华铁工贸公司",'
                   '"otherparty":"11",'
                   '"pctype":"12",'
                   '"plaintiff":"13",'
                   '"pplong":"2015-03-12",'
                   '"remark":"15",'
                   '"sourceid":"16",'
                   '"sourcen":"17",'
                   '"sslong":"2015-03-12",'
                   '"stype":2,'
                   '"title":"19",'
                   '"tribunal":"20",'
                   '"typet":31,'
                   '"typetname":"21",'
                   '"vprogram":"22",'
                   '"writtype":"23"}'
                   '],'
                           '"shixin":[],'
                           '"shenpan":[],'
                           '"zhixing":[],'
                           '"feizheng":[],'
                           '"qiankuan":[],'
                           '"qianshui":[],'
                           '"weifa":[],'
                           '"xianchu":[],'
                           '"xiangao":[],'
                           '"zuifan":[]'
                           '}'
                }

        r = requests.post(url=url, data=data)
        repones = r.text
        #print(r.text)
        print(repones)
        print(r.status_code)
    #单条监控录入接口
    # def test_monitorapi(self):
    #     url1 = 'http://localhost:6001/law/addwatch'
    #     data1 = {'n': '测试小微客户名称', 'id': '', 'customeruserid': '2', 'stype': '2'}
    #     r1 = requests.post(url=url1, data=data1)
    #     print(r1.text)
    #     print(r1.status_code)
    #精确查询接口
    # def test_custaccuratequery(self):
    #     conn = cx_Oracle.connect('law/law@10.138.22.223/edw')
    #     cursor = conn.cursor()
    #     cursor.execute("select cust_name from t_customer")
    #     row = cursor.fetchall()
    #     f = open('G:/工作资料/汇法网/7月27日上线版/20180801jar包newnew/logtest.txt', 'w')
    #     for username in row:
    #         print(username)
    #         print(username, file=f)
    #         url2 = 'http://localhost:6001/law/custaccuratequery'
    #         data2 = {'stype': '2', 'n': username, 'id': ''}
    #         r2 = requests.get(url=url2, params=data2)
    #         print(r2.text)
    #         print(r2.text, file=f)
    #         print(r2.status_code)
    #         sleep(2)
    #     f.close()
    #     conn.close()

    def tearDown(self):
        print("测试完毕！！！！！")


if __name__ == '__main__':
    unittest.main()