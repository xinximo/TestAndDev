import pytest

from test_web_weixin.page.main_page import MainPage


class TestAddMember:
    def setup_class(self):
        self.main = MainPage()

    @pytest.mark.parametrize("username,acctid,phone,expect_res", [("wx05", "005", "13011112225", "wx05"),
                                                                  ("wx06", "006", "13011112226", "wx06")])
    def test_add_member(self, username, acctid, phone, expect_res):
        # 添加成员测试用例
        # 1.跳转到添加成员页面 2.添加成员 3.自动跳转到通讯录页面
        res = self.main.goto_add_member().add_member(username, acctid, phone).get_member()
        assert expect_res in res

    @pytest.mark.parametrize("acctid, phone, expect_res",
                             [("004", "13011112224", '该手机已被“wx03”占有'),
                              ("001", "13011112226", '该帐号已被“wx”占有')])
    def test_add_member_fail(self, acctid, phone, expect_res):
        res = self.main.goto_add_member().add_member_fail(acctid, phone)
        assert expect_res in res

    @pytest.mark.skip
    def test_add_member_by_contact(self):
        res = self.main.goto_contact().goto_add_member().add_member().get_member()
        assert "wx" in res

    @pytest.mark.parametrize("depm,expect_res", [("wx17", "wx17")])
    def test_add_department(self, depm, expect_res):
        res = self.main.goto_contact().goto_add_Department().add_department(depm).get_department()
        assert expect_res in res

    def teardown(self):
        self.main.back_main()
