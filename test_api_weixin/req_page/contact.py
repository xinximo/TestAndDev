from typing import List

from test_api_weixin.req_page.base import Base


class Contact(Base):

    def create_member(self, userid: str, name: str, mobile: str, department: List[int], **kwargs):
        create_member_url = f"https://qyapi.weixin.qq.com/cgi-bin/user/create"
        proxies = {"https": "127.0.0.1:8888"}
        data = {
            "userid": userid,
            "name": name,
            "mobile": mobile,
            "department": department,
        }
        data.update(kwargs)
        r = self.s.post(create_member_url, json=data, proxies=proxies, verify=False)
        return r.json()

    def delete_member(self, userid):
        params = {"userid": userid}
        delete_member_url = f"https://qyapi.weixin.qq.com/cgi-bin/user/delete"
        r = self.s.get(delete_member_url, params=params)
        return r.json()

    def find_member(self, userid):
        params = {"userid": userid}
        find_member_url = f"https://qyapi.weixin.qq.com/cgi-bin/user/get"
        r = self.s.get(find_member_url, params=params)
        return r.json()

    def update_member(self, userid: str, name: str, mobile: str, department: List[int], **kwargs):
        updata_member_url = "https://qyapi.weixin.qq.com/cgi-bin/user/update"
        data = {
            "userid": userid,
            "name": name,
            "mobile": mobile,
            "department": department,
        }
        data.update(kwargs)
        r = self.s.post(updata_member_url, json=data)
        return r.json()
