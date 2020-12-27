from test_app_weixin.po.page.app import App
from test_app_weixin.po.page.main_page import MainPage


class TestContact:
    def test_add_member(self):
        main = App()
        main.start()
        main.goto_main().goto_address().click_addmember().add_member_manual().add_contact()
