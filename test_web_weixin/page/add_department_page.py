from selenium.webdriver.common.by import By

from test_web_weixin.page.base_page import BasePage
from test_web_weixin.page.contact_page import ContactPage


class AddDepartment(BasePage):
    _location_departname = (By.NAME, "name")
    _location_departlist = (By.CSS_SELECTOR, ".js_toggle_party_list")
    # _location_departID = (By.CSS_SELECTOR,'.form>:nth-child(3)>:nth-child(3) :nth-child(1)>:nth-child(3)')
    _location_departID = (By.CSS_SELECTOR, '.form [id = "1688853110157011_anchor"]')

    _location_departsubmit = (By.CSS_SELECTOR, 'a[d_ck="submit"]')

    def add_department(self, depm):
        # 添加部门
        self.find(self._location_departname).send_keys(depm)
        self.find(self._location_departlist).click()
        self.find(self._location_departID).click()
        """res_list = (self.finds(self._location_departID))
        res = [i for i in res_list]
        res[0].click()"""

        self.find(self._location_departsubmit).click()
        return ContactPage(self.driver)
