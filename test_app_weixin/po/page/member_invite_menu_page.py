from appium.webdriver.common.mobileby import MobileBy

from test_app_weixin.po.page.base_page import BasePage
from test_app_weixin.po.page.contact_add_page import ContactAddPage


class MemberInviteMenuPage(BasePage):
    """
    添加成员信息页面
    """

    def add_member_manual(self):
        """
        手动添加成员信息
        :return:
        """
        self.find_and_click(MobileBy.XPATH, "//*[@text='手动输入添加']")
        return ContactAddPage(self.driver)
