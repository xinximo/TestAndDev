import yaml
from selenium.webdriver.common.by import By

from test_app_frame_zuhe.page.market import Market
from test_app_frame_zuhe.page.pre_page import PrePage


class Main(PrePage):
    def goto_market(self):
        # self.find_and_click(By.XPATH, '//*[@resource-id="com.xueqiu.android:id/post_status"]')
        # self.find_and_click(By.XPATH, "//*[@resource-id='android:id/tabs']//*[@text='行情']")
        self.basepage.load("../page/main.yaml")
        return Market(self.basepage)
