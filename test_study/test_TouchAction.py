from selenium import webdriver
from selenium.webdriver import TouchActions
import time
import pytest

from selenium.webdriver.common.keys import Keys


class TestActionChains():
    def setup(self):
        option = webdriver.ChromeOptions()
        option.add_experimental_option('w3c', False)
        self.driver = webdriver.Chrome(options=option)
        self.driver.maximize_window()
        self.driver.get("http://www.baidu.com")
        self.driver.implicitly_wait(3)

    def teardown(self):
        self.driver.quit()

    def test_touch_action(self):
        ele = self.driver.find_element_by_id("kw")
        ele.send_keys("wx")
        click = self.driver.find_element_by_id("su")
        action = TouchActions(self.driver)
        action.tap(click)
        action.perform()
        action.scroll_from_element(ele, 0, 10000).perform()
