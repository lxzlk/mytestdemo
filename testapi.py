import requests
import unittest


class TestApi(unittest.TestCase):
    def setUp(self):
        print('start.....')

    def test_api(self):
        url = 'http://10.138.23.192:8080/api/blacklist.json'
        headers = {"name": "01484175",
                   "Content-Type": "application/json",
                   "sign": "8cf5f406d5ae028ebea99f4156006283"}
        data = {"commercialRegCert": "91500103742896264D",
                "custName": "重庆洪九果品股份有限公司",
                "timeStamp": "1526437520"
                }
        r = requests.post(url=url, json=data, headers=headers)
        repones = r.text
        #print(r.text)
        print(repones)
        print(r.status_code)

    def tearDown(self):
        print("测试完毕！！！！！")


if __name__ == '__main__':
    unittest.main()