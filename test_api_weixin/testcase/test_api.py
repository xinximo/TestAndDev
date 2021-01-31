import pytest

from test_api_weixin.req_page.contact import Contact


class TestContact:
    def setup_class(self):
        self.contact = Contact()

    @pytest.mark.parametrize("corpid,corpsecret,result", [(None, None, 0), ('xxx', None, 40013), (None, 'xxx', 40001)])
    def test_token(self, corpid, corpsecret, result):
        r = self.contact.get_token(corpid, corpsecret)
        assert r.get("errcode") == result

    def test_create(self):
        userid = "wx00123"
        name = "wx_00123"
        self.contact.create_member(userid=userid, name=name, mobile="13012348877", department=[4], alias={})
        try:
            find_result = self.contact.find_member(userid)
        finally:
            self.contact.delete_member(userid)
        assert find_result["name"] == name

    def test_update(self):
        userid = "wx00123"
        name = "wx_00123"
        update_name = "wx_00124"
        self.contact.create_member(userid=userid, name=name, mobile="13012348877", department=[4], alias={})
        self.contact.update_member(userid=userid, name=update_name, mobile="13012348877", department=[4], alias={})
        try:
            find_result = self.contact.find_member(userid)
        finally:
            self.contact.delete_member(userid)
        assert find_result["name"] == update_name

    @pytest.mark.parametrize("userid,name",
                             [("WangXin", "王鑫"), ("wx897949", "John Brewer"), ("a01", "a01"), ("001", "wx")])
    def test_find(self, userid, name):
        find_result = self.contact.find_member(userid)
        assert name in find_result["name"]

    def test_delete(self):
        userid = "wx00123"
        name = "wx_00123"
        self.contact.create_member(userid=userid, name=name, mobile="13012348877", department=[4], alias={})
        try:
            find_result = self.contact.find_member(userid)
        finally:
            self.contact.delete_member(userid)
        assert find_result["name"] == name
