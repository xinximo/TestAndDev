from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from test_web_weixin.page.base_page import BasePage


class ContactPage(BasePage):
    _location_member_list = (By.CSS_SELECTOR, ".member_colRight_memberTable_td:nth-child(2)")
    _location_goto_add_member = (By.CSS_SELECTOR, ".ww_operationBar .js_add_member")

    def goto_add_member(self):
        from test_web_weixin.page.add_member_page import AddMember
        # 通讯录添加成员操作
        self.wait_click(self._location_goto_add_member)
        # WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(
        #    (By.CSS_SELECTOR, '[class="js_operationBar_footer ww_operationBar"] a:nth-child(2)')))
        self.find(self._location_goto_add_member).click()
        return AddMember(self.driver)

    def get_member(self):
        # 获取成员列表,用来做断言信息
        member_list = self.finds(self._location_member_list)
        member_list_res = [i.text for i in member_list]
        """
        member_list2 = []
        for i in member_list:
            member_list2.append(i.text)
        """

        return member_list_res
