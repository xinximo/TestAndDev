import yaml
from appium.webdriver import WebElement
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from test_app_frame.black_handle import black_wrapper


class BasePage:
    FIND = 'find'
    ACTION = 'action'
    CONTENT = 'content'
    FIND_AND_CLICK = 'find_and_click'
    SEND = 'send'

    def __init__(self, driver: WebDriver = None):
        self.driver = driver
        # 参考：黑名单类
        self.black_list = [(By.XPATH, "//*[@resource-id='com.xueqiu.android:id/iv_close']")]

    # 设计模式：代理模式，装饰器模式
    # 装饰器
    @black_wrapper
    def find(self, by, locator):

        return self.driver.find_element(by, locator)

    def finds(self, by, locator):
        return self.driver.find_elements(by, locator)

    def find_and_click(self, by, locator):
        self.find(by, locator).click()

    def send(self, by, locator, content):
        self.find(by, locator).send_keys(content)

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

    @staticmethod
    def find_by_swip2(driver: WebDriver, by, locator) -> WebElement:
        driver.implicitly_wait(1)
        elements = driver.find_elements(by, locator)
        while len(elements) == 0:
            driver.swipe(0, 600, 0, 400)
            elements = driver.find_elements(by, locator)
        driver.implicitly_wait(5)
        return elements[0]

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

    def load(self, yaml_path):
        with open(yaml_path, encoding="utf-8") as f:
            data = yaml.load(f)
        for step in data:
            xpath_expr = step.get(self.FIND)
            action = step.get(self.ACTION)
            content = step.get(self.CONTENT)
            if action == self.FIND_AND_CLICK:
                self.find_and_click(By.XPATH, xpath_expr)
            elif action == self.SEND:
                self.send(By.XPATH, xpath_expr, content)

    def screenshot(self, picture_path):
        self.driver.save_screenshot(picture_path)

    def teardown(self):
        self.driver.quit()
