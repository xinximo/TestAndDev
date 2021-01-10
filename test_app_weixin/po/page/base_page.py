from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from test_app_weixin.po.page.black_handle import black_wrapper


class BasePage:
    def __init__(self, driver: WebDriver = None):
        self.driver = driver
        # 参考:黑名单类
        self.black_list = [(By.XPATH, "")]

    @black_wrapper
    def find(self, by, locator):
        return self.driver.find_element(by, locator)

    def finds(self, by, locator):
        return self.driver.find_elements(by, locator)

    def find_and_click(self, by, locator):
        self.find(by, locator).click()

    def scroll_find(self, text):
        return self.driver.find_element(MobileBy.
                                        ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().'
                                                             'scrollable(true).instance(0)).'
                                                             'scrollIntoView(new UiSelector().'
                                                             f'text("{text}").instance(0));')

    def scroll_find_click(self, text):
        self.scroll_find(text).click()

    def swipe_find(self, by, locator):
        self.driver.implicitly_wait(1)
        eles = self.driver.find_elements(by, locator)
        while len(eles) == 0:
            self.driver.swipe(0, 600, 0, 400)
            eles = self.driver.find_elements(by, locator)
        self.driver.implicitly_wait(5)
        return eles[0]

    def swipe_find_click(self, by, locator):
        self.swipe_find(by, locator).click()

    def find_and_send(self, by, locator, text):
        self.find(by, locator).send_keys(text)

    def wait_for(self, by, locator):
        def wait_ele_for(driver: WebDriver):
            eles = driver.find_elements(by, locator)
            return len(eles) > 0

        WebDriverWait(self.driver, 30).until(wait_ele_for)

    def get_toast_text(self):
        result = self.find(MobileBy.XPATH, "//*[@class='android.widget.Toast']").text
        return result

    def teardown(self):
        self.driver.quit()
