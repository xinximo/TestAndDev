from selenium import webdriver
from selenium.webdriver import ActionChains
import time
import pytest

from selenium.webdriver.common.keys import Keys


class TestActionChains():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("http://www.baidu.com")

    def teardown(self):
        self.driver.quit()

    @pytest.mark.skip
    def test_case_move(self):
        click = self.driver.find_element_by_xpath('//*[@id="s-usersetting-top"]')
        action = ActionChains(self.driver)  # 实例化actionchains
        action.move_to_element(click)
        action.perform()
        time.sleep(3)

    def test_case_input(self):
        click = self.driver.find_element_by_id("kw")
        action = ActionChains(self.driver)
        action.click(click)
        action.send_keys("123").pause(1)
        action.send_keys(Keys.BACK_SPACE).pause(1)
        action.send_keys(Keys.SPACE).pause(1)
        action.send_keys("wx").pause(1)
        action.send_keys(Keys.ENTER).pause(1)
        action.perform()
