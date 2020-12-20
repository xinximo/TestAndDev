import random

from faker import Faker
from selenium import webdriver
from selenium.webdriver.common.by import By

from test_web_weixin.page.base_page import BasePage
from test_web_weixin.page.contact_page import ContactPage


class AddMember(BasePage):
    _location_username = (By.ID, "username")
    _location_acctid = (By.ID, "memberAdd_acctid")
    _location_Add_phone = (By.ID, "memberAdd_phone")
    _location_sava = (By.CSS_SELECTOR, '[class="js_member_editor_form"]>div:nth-child(3)>a:nth-child(2)')

    def add_member(self):
        # 添加成员
        self.find(self._location_username).send_keys("wx")
        self.find(self._location_acctid).send_keys("001")
        self.find(self._location_Add_phone).send_keys("13011112222")
        self.find(self._location_sava).click()
        return ContactPage(self.driver)

    def add_member_fail(self, acctid, phone):
        # 添加成员失败操作
        self.find(self._location_username).send_keys("wx")
        self.find(self._location_acctid).send_keys(acctid)
        self.find(self._location_Add_phone).send_keys(phone)
        self.find(self._location_sava).click()
        res = self.finds(By.CSS_SELECTOR, ".ww_inputWithTips_tips")
        print(res)
        error_list = [i.text for i in res]
        print(error_list)
        return error_list
