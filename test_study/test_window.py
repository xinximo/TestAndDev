import time

from selenium import webdriver


class Testwindows():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("http://www.baidu.com")
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_windows(self):
        self.driver.find_element_by_link_text("登录").click()
        self.driver.find_element_by_link_text("立即注册").click()
        print(self.driver.current_window_handle)  # 获取当前窗口
        print(self.driver.window_handles)  # 获取全部窗口
        self.driver.switch_to.window(self.driver.window_handles[1])  # 切换到第二个窗口
        self.driver.find_element_by_id("TANGRAM__PSP_4__userName").send_keys("wx")
        self.driver.find_element_by_id("TANGRAM__PSP_4__phone").send_keys("123456")
        self.driver.find_element_by_id("login_btn").click()
        self.driver.find_element_by_id("TANGRAM__PSP_28__footerULoginBtn").click()
        self.driver.switch_to.window(self.driver.window_handles[0])  # 切换到第一个窗口
        self.driver.find_element_by_id("TANGRAM__PSP_11__footerULoginBtn").click()
        self.driver.find_element_by_id("TANGRAM__PSP_11__userName").send_keys("wx")
        self.driver.find_element_by_id("TANGRAM__PSP_11__password").send_keys("wx")
        self.driver.find_element_by_id("TANGRAM__PSP_11__submit").click()

        time.sleep(3)
