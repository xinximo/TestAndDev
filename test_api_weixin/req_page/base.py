import requests


class Base:
    def __init__(self):
        self.s = requests.Session()
        self.corpid = 'wwcd8bdf71f69a6d0c'
        self.corpsecret = '3kjbx36sJZLhGjaboMlO_rsuHAWOj4ILZTtXGuYUQ1s'
        self.s.params["access_token"] = self.get_token()['access_token']

    def get_token(self, corpid=None, corpsecret=None):
        proxies = {"https": "127.0.0.1:8888"}
        if corpid is None:
            corpid = self.corpid
        if corpsecret is None:
            corpsecret = self.corpsecret
        params = {"corpid": corpid, "corpsecret": corpsecret}
        r = requests.get(f"https://qyapi.weixin.qq.com/cgi-bin/gettoken", params=params, proxies=proxies, verify=False)
        # token = r.json()['access_token']
        return r.json()
