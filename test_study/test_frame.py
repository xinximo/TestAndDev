import time

from test_study.Base import Base


class TestFrame(Base):
    def test_frame(self):
        self.driver.get("http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable")
        self.driver.switch_to.frame("iframeResult")  # 切换到指定的frame
        print(self.driver.find_element_by_id("draggable").text)
        # self.driver.switch_to.parent_frame()#切换到父级frame
        self.driver.switch_to.default_content()  # 切换到默认frame
        self.driver.find_element_by_id("submitBTN").click()
        time.sleep(3)
