from test_app_weixin.po.page.base_page import BasePage
from test_app_weixin.po.page.member_invite_menu_page import MemberInviteMenuPage


class AddressListPage(BasePage):
    """
    通讯录页面
    """

    def click_addmember(self):
        """
        添加成员
        :return:
        """
        self.scroll_find_click("添加成员")
        return MemberInviteMenuPage(self.driver)
