import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from test_web_weixin.page.base_page import BasePage


class ContactPage(BasePage):
    _location_member_list = (By.CSS_SELECTOR, ".member_colRight_memberTable_td:nth-child(2)")
    _location_goto_add_member = (By.CSS_SELECTOR, ".ww_operationBar .js_add_member")
    _location_goto_add_department = (By.CSS_SELECTOR, ".js_create_dropdown")
    _location_goto_add_depart = (By.CSS_SELECTOR, ".js_create_party")
    _location_departlist = (By.CSS_SELECTOR, '.jstree-children a:nth-child(3)')

    def goto_add_member(self):
        from test_web_weixin.page.add_member_page import AddMember
        # 通讯录添加成员操作
        self.wait_click(self._location_goto_add_member)
        # WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(
        #    (By.CSS_SELECTOR, '[class="js_operationBar_footer ww_operationBar"] a:nth-child(2)')))
        self.find(self._location_goto_add_member).click()
        return AddMember(self.driver)

    def goto_add_Department(self):
        from test_web_weixin.page.add_department_page import AddDepartment
        self.find(self._location_goto_add_department).click()
        self.find(self._location_goto_add_depart).click()
        return AddDepartment(self.driver)

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

    def get_department(self):
        # 获取部门列表,用来做断言信息
        time.sleep(1)
        self.driver.refresh()
        department_list = self.finds(self._location_departlist)
        department_list_res = [i.text for i in department_list]
        return department_list_res
