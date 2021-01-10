# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python
import pytest
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.wait import WebDriverWait


class TestXueqiu:
    def setup(self):
        # nox_adb.exe devices
        # adb connect 127.0.0.1:7555
        # nox_adb.exe connect 127.0.0.1:62001
        caps = {}
        caps["platformName"] = "Android"
        caps["deviceName"] = "xueqiu"
        caps["appPackage"] = "com.xueqiu.android"
        caps["appActivity"] = ".common.MainActivity"
        caps["noReset"] = "true"
        caps["ensureWebviewsHavePages"] = True
        # 设置页面等待空闲状态的时间
        caps['settings[waitForIdleTimeout]'] = 0
        caps['skipDeviceInitialization'] = "true"
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_Select(self):
        self.driver.find_element(MobileBy.ID, "com.xueqiu.android:id/tv_search").click()
        self.driver.find_element(MobileBy.ID, "com.xueqiu.android:id/search_input_text").send_keys("alibaba")
        self.driver.find_element(MobileBy.XPATH, "//*[@text='阿里巴巴']").click()
        WebDriverWait(self.driver, 10).until(lambda x: "阿里巴巴" in x.page_source)
        assert "阿里巴巴" in self.driver.page_source

    def test_attr(self):
        ele = self.driver.find_element(MobileBy.ID, "com.xueqiu.android:id/tv_search")
        search_enabled = ele.is_enabled()
        print(ele.text)
        print(ele.location)
        print(ele.size)
        if search_enabled == True:
            ele.click()
            self.driver.find_element(MobileBy.ID, "com.xueqiu.android:id/search_input_text").send_keys("alibaba")
            ele_ali = self.driver.find_element(MobileBy.XPATH, "//*[@text='阿里巴巴']")
            ele_play = ele_ali.get_attribute("displayed")
            if ele_play == 'true':
                print("搜索成功")
            else:
                print("搜索失败")

    def test_touchaction(self):
        action = TouchAction(self.driver)
        windows_rect = self.driver.get_window_rect()
        width = windows_rect['width']
        height = windows_rect['height']
        x1 = int(width / 2)
        y_start = int(height * 4 / 5)
        y_end = int(height * 1 / 5)
        action.press(x=x1, y=y_start).wait(200).move_to(x=x1, y=y_end).wait(200).release().perform()  # 点击坐标后移动释放并执行

    def test_myinfo(self):
        """

        :return:
        """
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("我的")').click()
        self.driver.find_element_by_android_uiautomator('new UiSelector().textContains("账号密码")').click()
        self.driver.find_element_by_android_uiautomator(
            'new UiSelector().resourceId("com.xueqiu.android:id/login_account")').send_keys('123456')
        self.driver.find_element_by_android_uiautomator(
            'new UiSelector().resourceId("com.xueqiu.android:id/login_password")').send_keys('123456')

    def test_scroll_find_element(self):
        self.driver.find_element_by_android_uiautomator('new UiScrollable(new UiSelector().'
                                                        'scrollable(true).instance(0)).'
                                                        'scrollIntoView(new UiSelector().text("杭州王大磊").'
                                                        'instance(0));')


if __name__ == '__main__':
    pytest.main()
