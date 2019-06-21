from selenium import webdriver
import unittest
from HtmlTestRunner import HTMLTestRunner

class Badidu(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.base_url = "http://www.baidu.com"

    def test_Baidu_search(self):
        driver = self.driver
        driver.get(self.base_url)
        driver.find_element_by_id("kw").send_keys("HTMLTestRunner")
        driver.find_element_by_id("su").click()

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':

    testunit = unittest.TestSuite()
    testunit.addTest(Badidu("test_baidu_search"))

    fp = open('./result.html','wb')

    runner = HTMLTestRunner(stream=fp,
                            title='百度搜索报告',
                            description='用例执行情况：')
    runner.run(testunit)
    fp.close()
##测试vscode