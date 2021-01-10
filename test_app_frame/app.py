from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy

from test_app_frame.base_page import BasePage
from test_app_frame.page.main import Main


class App(BasePage):
    def start(self):
        if self.driver is None:
            caps = {}
            caps["platformName"] = "Android"
            caps["deviceName"] = "xueqiu"
            caps["appPackage"] = "com.xueqiu.android"
            caps["appActivity"] = ".view.WelcomeActivityAlias"
            caps["noReset"] = "true"
            caps["ensureWebviewsHavePages"] = True
            # 设置页面等待空闲状态的时间
            caps['settings[waitForIdleTimeout]'] = 0
            self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        else:
            self.driver.launch_app()
        self.driver.implicitly_wait(10)
        return self

    def restart(self):
        # 重启 app
        self.driver.close_app()
        self.driver.launch_app()
        pass

    def stop(self):
        # 停止 app
        self.driver.quit()

    def goto_main(self):
        return Main(self.driver)
