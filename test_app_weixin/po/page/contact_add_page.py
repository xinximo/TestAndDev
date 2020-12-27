from appium.webdriver.common.mobileby import MobileBy

from test_app_weixin.po.page.base_page import BasePage


class ContactAddPage(BasePage):
    """
    成员信息编辑页面
    """

    def add_contact(self):
        """
        编辑成员信息
        :return:
        """
        self.find_and_send(MobileBy.XPATH, "//*[contains(@text,'姓名')]/..//*[@text='必填']", "a01")
        self.find_and_click(MobileBy.XPATH, "//*[contains(@text,'性别')]/..//*[@text='男']")
        self.wait_for(MobileBy.XPATH, "//*[@text='女']")
        self.find_and_click(MobileBy.XPATH, "//*[@text='女']")
        self.find_and_send(MobileBy.XPATH, "//*[contains(@text,'手机')]/..//*[@text='手机号']", "13000000001")
        self.find_and_click(MobileBy.XPATH, "//*[@text='保存']")
