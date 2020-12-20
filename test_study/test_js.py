import time
import pytest
from test_study.Base import Base


class Testjs(Base):
    @pytest.mark.skip
    def test_js_scroll(self):
        self.driver.get("http://www.baidu.com")
        self.driver.find_element_by_id("kw").send_keys("python")
        # self.driver.find_element_by_id("su").click()
        a = self.driver.execute_script("return document.getElementById('su')")
        a.click()
        self.driver.execute_script("document.documentElement.scrollTop=10000")  # 滑动到底部
        self.driver.find_element_by_xpath('//*[@id="page"]//a[10]').click()
        time.sleep(3)
        for code in ['return document.title', 'return JSON.stringify(performance.timing)']:  # 返回JS执行结果
            print(self.driver.execute_script(code))

    def test_date(self):
        self.driver.get("https://www.12306.cn/index/")
        ele = self.driver.execute_script("a=document.getElementById('train_date');a.removeAttribute('readonly')")
        self.driver.execute_script("a=document.getElementById('train_date');a.value='2020-08-08'")
        print(self.driver.execute_script("return document.getElementById('train_date').value"))
        time.sleep(3)
