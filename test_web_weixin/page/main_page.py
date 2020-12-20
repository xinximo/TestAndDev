from selenium import webdriver
from selenium.webdriver.common.by import By

from test_web_weixin.page.add_member_page import AddMember
from test_web_weixin.page.base_page import BasePage
from test_web_weixin.page.contact_page import ContactPage


class MainPage(BasePage):
    _location_goto_member = (By.XPATH, '//*[@class="index_service_cnt js_service_list"]/a[1]//span[1]')

    def goto_add_member(self):
        # 跳转添加成员
        # 解元祖操作
        self.find(self._location_goto_member).click()
        return AddMember(self.driver)

    def goto_contact(self):
        # 跳转到通讯录页面
        self.find(By.ID, "menu_contacts").click()
        return ContactPage(self.driver)

    def back_main(self):
        self.driver.find_element(By.ID, "menu_index").click()
        self.find(By.CSS_SELECTOR, "a[node-type='cancel'").click()
