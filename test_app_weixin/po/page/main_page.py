from appium.webdriver.common.mobileby import MobileBy

from test_app_weixin.po.page.address_list_page import AddressListPage
from test_app_weixin.po.page.base_page import BasePage


class MainPage(BasePage):
    """
    首页po
    """

    def goto_address(self):
        """
        进入通讯录
        :return:
        """
        self.find_and_click(MobileBy.XPATH, "//*[@text='通讯录' and @resource-id='com.tencent.wework:id/elq']")

        return AddressListPage(self.driver)
