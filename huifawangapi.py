import requests
import unittest


class TestApi(unittest.TestCase):
    def setUp(self):
        print('start.....')

    def test_api(self):
        url = 'http://testapi.lawxp.com/s.aspx?'
        #headers = {"Content-Type": "application/json"}
        data = {'conid': '1023', 'smodel': '102', 'pg': '1', 'pz': '100'}
        r = requests.post(url=url, data=data)
        repones = r.text
        print(r)
        print("1023返回:", repones)
        print("1023:", r.status_code)
        data1 = {'conid': '1034', 'n': '陈灿林', 'id': '420204196904184538'}
        r1034 = requests.get(url=url, params=data1)
        requests1= r1034.text
        print("1034返回：", requests1)

    def tearDown(self):
        print("测试完毕！！！！！")


if __name__ == '__main__':
    unittest.main()