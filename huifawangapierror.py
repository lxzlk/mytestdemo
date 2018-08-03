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
                           '"keyid":"9999999908",'
                           '"money":"8",'
                           '"monitorid":"9",'
                           '"name":"重庆百福润商贸有限公司",'
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
                           '"writtype":"23"}],'
                           '"shixin":[],'
                           '"shenpan":[],'
                           '"zhixing":[],'
                           '"feizheng":[],'
                           '"qiankuan":[],'
                           '"qianshui":[],'
                           '"weifa":[],'
                           '"xianchu":[],'
                           '"xiangao":[{"sourcen": "999999",'
                           '"sourceid": "009999",'
                           '"stype": 2,'
                           '"monitorid": "90",'
                           '"pplong": "2015-09-23",'
                           '"keyid": 999999909,'
                           '"typet": 151,'
                           '"typetname": "限高",'
                           '"title": "该条信息标题",'
                           '"sslong": "2001-04-20",'
                           '"name": "重庆百福润商贸有限公司",'
                           '"id": "",'
                           '"casenum":"：(2013)坊法执字第00252号 ",'
                           '"court": "潍坊市坊子区人民法院 ",'
                           '"content":"测试审判结果",'
                           '"timetype":"2013年5月",'
                           '"remark":"该信息的立案时间晚于官方发布信息，经核查最高院的失信被执行人网站，网站原数据就是如此记载，特此提请注意。",'
                           '"state":"执行中"}'
                           '],'
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
    #     data1 = {'n': '测试一二三四五六七八九十', 'id': '', 'customeruserid': '6', 'stype': '2'}
    #     r1 = requests.post(url=url1, data=data1)
    #     print(r1.text)
    #     print(r1.status_code)

    #单条监控录入接口批量处理
    # def test_monitorapibatch(self):
    #     url1 = 'http://localhost:6001/law/addwatch'
    #     with open('G:/工作资料/汇法网/7月27日上线版/20180801jar包newnew/cust_name.txt', encoding='utf-8') as f:
    #         for i in f.readlines()[1:]:
    #             j = i.strip()
    #             print(j)
    #             data1 = {'n': j, 'id': '', 'customeruserid': '2', 'stype': '2'}
    #             r1 = requests.post(url=url1, data=data1)
    #             print(r1.text)
    #             print(r1.status_code)
    #             sleep(2)

    #精确查询接口读数据库批量
    # def test_custaccuratequeryconn(self):
    #     conn = cx_Oracle.connect('law/law@10.138.22.223/edw')
    #     cursor = conn.cursor()
    #     cursor.execute("select cust_name from t_customer where id>990")
    #     row = cursor.fetchall()
    #     f = open('G:/工作资料/汇法网/7月27日上线版/20180801jar包newnew/logtest.txt', 'w', encoding='utf-8')
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

    # 精确查询接口
    # def test_custaccuratequery(self):
    #
    #     url3 = 'http://localhost:6001/law/custaccuratequery'
    #     data3 = {'stype': '2', 'n': '中国天楹股份有限公司', 'id': ''}
    #     r3 = requests.get(url=url3, params=data3)
    #     print(r3.text)
    #     print(r3.status_code)
    #     sleep(3)

    def tearDown(self):
        print("测试完毕！！！！！")


if __name__ == '__main__':
    unittest.main()