import pytest

from test_web_weixin.page.main_page import MainPage


class TestAddMember:
    def setup_class(self):
        self.main = MainPage()

    def test_add_member(self):
        # 添加成员测试用例
        # 1.跳转到添加成员页面 2.添加成员 3.自动跳转到通讯录页面
        res = self.main.goto_add_member().add_member().get_member()
        assert "wx" in res

    @pytest.mark.parametrize("acctid,phone,expect_res", [("001", "13011112222", '该账户已被"wx"占用')])
    def test_add_member_fail(self, acctid, phone, expect_res):
        res = self.main.goto_add_member().add_member_fail(acctid, phone)
        assert res == expect_res

    def test_add_member_by_contact(self):
        res = self.main.goto_contact().goto_add_member().add_member().get_member()
        assert "wx" in res

    def teardown_class(self):
        self.main.back_main()
