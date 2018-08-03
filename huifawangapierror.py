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
    #���ͽӿ�
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
                           '"name":"����ٸ�����ó���޹�˾",'
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
                           '"typetname": "�޸�",'
                           '"title": "������Ϣ����",'
                           '"sslong": "2001-04-20",'
                           '"name": "����ٸ�����ó���޹�˾",'
                           '"id": "",'
                           '"casenum":"��(2013)����ִ�ֵ�00252�� ",'
                           '"court": "Ϋ���з���������Ժ ",'
                           '"content":"�������н��",'
                           '"timetype":"2013��5��",'
                           '"remark":"����Ϣ������ʱ�����ڹٷ�������Ϣ�����˲����Ժ��ʧ�ű�ִ������վ����վԭ���ݾ�����˼��أ��ش�����ע�⡣",'
                           '"state":"ִ����"}'
                           '],'
                           '"zuifan":[]'
                           '}'
                }

        r = requests.post(url=url, data=data)
        repones = r.text
        #print(r.text)
        print(repones)
        print(r.status_code)
    #�������¼��ӿ�
    # def test_monitorapi(self):
    #     url1 = 'http://localhost:6001/law/addwatch'
    #     data1 = {'n': '����һ�����������߰˾�ʮ', 'id': '', 'customeruserid': '6', 'stype': '2'}
    #     r1 = requests.post(url=url1, data=data1)
    #     print(r1.text)
    #     print(r1.status_code)

    #�������¼��ӿ���������
    # def test_monitorapibatch(self):
    #     url1 = 'http://localhost:6001/law/addwatch'
    #     with open('G:/��������/�㷨��/7��27�����߰�/20180801jar��newnew/cust_name.txt', encoding='utf-8') as f:
    #         for i in f.readlines()[1:]:
    #             j = i.strip()
    #             print(j)
    #             data1 = {'n': j, 'id': '', 'customeruserid': '2', 'stype': '2'}
    #             r1 = requests.post(url=url1, data=data1)
    #             print(r1.text)
    #             print(r1.status_code)
    #             sleep(2)

    #��ȷ��ѯ�ӿڶ����ݿ�����
    # def test_custaccuratequeryconn(self):
    #     conn = cx_Oracle.connect('law/law@10.138.22.223/edw')
    #     cursor = conn.cursor()
    #     cursor.execute("select cust_name from t_customer where id>990")
    #     row = cursor.fetchall()
    #     f = open('G:/��������/�㷨��/7��27�����߰�/20180801jar��newnew/logtest.txt', 'w', encoding='utf-8')
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

    # ��ȷ��ѯ�ӿ�
    # def test_custaccuratequery(self):
    #
    #     url3 = 'http://localhost:6001/law/custaccuratequery'
    #     data3 = {'stype': '2', 'n': '�й���麹ɷ����޹�˾', 'id': ''}
    #     r3 = requests.get(url=url3, params=data3)
    #     print(r3.text)
    #     print(r3.status_code)
    #     sleep(3)

    def tearDown(self):
        print("������ϣ���������")


if __name__ == '__main__':
    unittest.main()