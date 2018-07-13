import unittest
from selenium import webdriver


class LoginTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def login(self, username, password):
        self.driver.get("http://10.138.25.74:8100/html/login.html")
        self.driver.find_element_by_name('username').send_keys(username)
        self.driver.find_element_by_id('loginpwd').send_keys(password)
        self.driver.find_element_by_xpath('//*[@id="login"]/button').click()

    def test_login_success(self):
        self.login('test', '123Abc')

    def tearDown(self):
        print("测试完成！！！！！！！！！")
        print('python'[::2])


if __name__ == '__main__':
    unittest.main()