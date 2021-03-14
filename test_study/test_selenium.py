import allure
import selenium
from selenium import webdriver

@allure.feature("测试类")
class Test_Demo():
    @allure.story("测试用例1")
    def test_selenium(self):
        driver = webdriver.Chrome()
        driver.get("http://www.baidu.com")

    @allure.story("测试用例2")
    def test_wx1(self):
        pass
