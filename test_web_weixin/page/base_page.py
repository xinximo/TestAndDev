import pytest
import yaml
from selenium import webdriver
import os

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __int__(self, base_driver=None):
        # 注解，不是赋值操作。用作ide的类型提示
        base_driver: WebDriver
        if base_driver is None:
            self.driver = webdriver.Chrome()
            self.driver.maximize_window()
            self.driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx")
            self._test_login()
        else:
            self.driver = base_driver
        self.driver.implicitly_wait(3)

    """
    def setup_class(self):
        opt = webdriver.ChromeOptions()
        opt.debugger_address = '127.0.0.1:9927'  # 设置debug地址 # chrome --remote-debugging-port=9927
        driver = webdriver.Chrome(options=opt)
        driver.implicitly_wait(5)
        driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        #driver.find_element_by_id("menu_contacts").click()
        cookie = driver.get_cookies()
        with open("wx_cookie.yml", "w", encoding="UTF-8") as f:
            yaml.dump(cookie, f)
    """

    def _test_login(self):
        with open("data_cookie.yml", "r", encoding="UTF-8") as f:
            yaml_data = yaml.safe_load(f)
        for cookie in yaml_data:
            self.driver.add_cookie(cookie)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")

    def find(self, by, value=None):
        if value is None:
            return self.driver.find_element(*by)
        else:
            return self.driver.find_element(by=by, value=value)

    def finds(self, by, value):
        if value is None:
            return self.driver.find_elements(*by)
        else:
            return self.driver.find_elements(by=by, value=value)

    def wait_click(self, locator):
        return WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(locator))

    def quit(self):
        self.driver.quit()
