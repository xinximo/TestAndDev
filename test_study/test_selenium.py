import allure
import selenium
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

@allure.feature("测试类")
class Test_Demo():
    @allure.story("测试用例1")
    def test_selenium(self):
        driver = webdriver.Remote(
            command_executor='http://localhost:5001/wd/hub',
            desired_capabilities=DesiredCapabilities.CHROME)
        #driver = webdriver.Chrome()
        driver.get("http://www.baidu.com")
        driver.close()

    @allure.story("测试用例2")
    def test_wx1(self):
        pass

    @allure.story("测试用例1")
    def test_selenium2(self):
        driver = webdriver.Remote(
            command_executor='http://localhost:5001/wd/hub',
            desired_capabilities=DesiredCapabilities.CHROME)
        # driver = webdriver.Chrome()
        driver.get("http://www.baidu.com")
        driver.close()

    @allure.story("测试用例2")
    def test_wx2(self):
        pass
    #并发测试 pytest -n 3 test_selenium.py
