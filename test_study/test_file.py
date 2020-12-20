import time

import pytest
from selenium.webdriver import ActionChains

from test_study.Base import Base


class TestFile(Base):
    @pytest.mark.skip
    def test_file_upload(self):
        self.driver.get("https://image.baidu.com/")
        self.driver.find_element_by_xpath('//*[@id="sttb"][1]').click()
        self.driver.find_element_by_id('uploadImg').send_keys("E:\图片1.png")  # 上传图片
        time.sleep(3)

    @pytest.mark.skip
    def test_alert(self):
        self.driver.get("http://www.baidu.com")
        self.driver.execute_script('window.alert("这是一个弹框")')
        a = self.driver.switch_to.alert.text
        self.driver.switch_to.alert.accept()
        print(a)
        time.sleep(5)

    def test_Alert(self):
        self.driver.get("http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable")
        self.driver.switch_to.frame("iframeResult")  # 切换到指定的frame
        action = ActionChains(self.driver)
        drag = self.driver.find_element_by_id("draggable")
        drop = self.driver.find_element_by_id("droppable")
        action.drag_and_drop(drag, drop).perform()  # 拖动元素
        self.driver.switch_to.alert.accept()  # 弹框确认
        print("弹框确认成功")
        # self.driver.switch_to.parent_frame()#切换到父级frame
        self.driver.switch_to.default_content()  # 切换到默认frame
        self.driver.find_element_by_id("submitBTN").click()
        time.sleep(3)
