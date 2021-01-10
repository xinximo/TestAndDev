import yaml
from selenium.webdriver.common.by import By

from test_app_frame_zuhe.page.search import Search
from test_app_frame_zuhe.page.pre_page import PrePage


class Market(PrePage):
    def goto_search(self):
        # self.find_and_click(By.XPATH, "//*[@resource-id='com.xueqiu.android:id/action_search']")
        self.basepage.load("../page/market.yaml")
        return Search(self.basepage)
