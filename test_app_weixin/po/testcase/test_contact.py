from test_app_weixin.po.page.app import App
from test_app_weixin.po.page.main_page import MainPage


class TestContact:
    def setup(self):
        self.main = App()
        self.main.start()

    def test_add_member(self):
        self.main.goto_main().goto_address().click_addmember().add_member_manual().add_contact()
