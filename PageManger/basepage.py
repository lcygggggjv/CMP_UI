import time
import ddddocr
import pytest
import requests
from PIL import Image
from Config.read_env import EnvironMent
from playwright.sync_api import *
import io
from Config.file_path import FilePath
import allure
from hamcrest import assert_that, equal_to
import easyocr


class BasePage:

    def __init__(self):

        """with sync_playwright() as p:  不用with语句, 不用无头模式，将窗口最大化"""

        self.env = EnvironMent()
        p = sync_playwright().start()
        browser = p.chromium.launch(headless=False, args=['--start-maximized'])
        context = browser.new_context(no_viewport=True)
        self.page = context.new_page()
        self.login()

    def login(self):
        """登录"""

        self.page.goto(self.env.url())
        self.page.locator('//input[@placeholder="账号"]').fill(self.env.account())
        self.page.locator('//input[@placeholder="密码"]').fill(self.env.password())
        self.page.locator('//img[@class="login-code-img"]').screenshot(path=FilePath.captcha_dir)
        captcha = self.ocr_captcha()
        # captcha = self.easy_ocr()
        self.page.locator('//input[@placeholder="验证码"]').fill(captcha)
        self.page.locator("//span[text()='登 录']").click()
        if self.loop_assert("//p[text()='验证码错误']"):
            self.page.locator('//img[@class="login-code-img"]').screenshot(path=FilePath.captcha_dir)
            captcha = self.ocr_captcha()
            self.page.locator('//input[@placeholder="验证码"]').fill(captcha)
            self.page.locator("//span[text()='登 录']").click()

    def gt_guide_page(self):
        """固投引导页 储备库列表"""
        self.page.locator("(//p[text()='储备库'])[1]").click()

    def assert_allure_screenshot(self, actual, expected):

        try:
            assert_that(actual, equal_to(expected))
        except AssertionError as e:
            img = self.page.screenshot()
            allure.attach(img, name="用例失败截图", attachment_type=allure.attachment_type.PNG)
            raise AssertionError(f"断言失败：预期结果：{expected} ,!= 实际结果：{actual}") from e

    def loop_assert(self, locator):
        """循环校验，alert文本框"""
        for i in range(20):
            actual_info = self.page.locator(locator).is_visible()
            # print(f"这是实际{actual_info}, 第{i}次")
            if actual_info:
                return actual_info
            # time.sleep(1)

    def loop_find_locator(self, locator):
        """循环校验，alert文本框"""
        for i in range(30):
            actual_info = self.page.query_selector_all(locator)
            # print(f"这是实际{actual_info}, 第{i}次")
            if actual_info:
                return actual_info
            time.sleep(1)

    def loop_find_locator_two(self, locator1, locator2):
        """循环校验，alert文本框"""
        for i in range(30):
            actual1 = self.page.query_selector_all(locator1)
            actual2 = self.page.query_selector_all(locator2)
            # print(f"这是实际{actual_info}, 第{i}次")
            if actual1 and actual2:
                return actual1, actual2
            time.sleep(1)

    def loop_find_locator2(self, locator):
        """循环校验，alert文本框"""
        count = 0
        while count < 30:
            # print(f"这是实际{actual_info}, 第{i}次")
            actual_info = self.page.query_selector_all(locator)
            if actual_info:
                return actual_info
            time.sleep(1)
            count += 1

    @staticmethod
    def get_captcha():
        """通过接口获取验证码"""
        res = requests.get(url='http://192.168.211.21:8088/ctrm/huanghe/login/captcha')
        ss = res.content
        return ss

    @staticmethod
    def ocr_captcha():
        """通过ocr识别接口数据, rb是读取二进制数据
            这一行使用PIL的Image.open()方法，配合io.BytesIO
            将刚刚读取的二进制数据转换成一个可以在内存中操作的图像对象
        """
        ocr = ddddocr.DdddOcr()
        with open(FilePath.captcha_dir, 'rb') as f:
            img_bytes = f.read()

        img = Image.open(io.BytesIO(img_bytes))
        data = ocr.classification(img)
        return data

    @staticmethod
    def easy_ocr():

        reader = easyocr.Reader(['en'])
        res = reader.readtext(FilePath.captcha_dir)
        for detection in res:
            print(detection[1])
            return detection[1]

    def captcha_response(self, response):
        """获取验证码接口数据"""
        if '/login/captcha' in response.url:
            self.captcha_data = response.json()


if __name__ == '__main__':

    ad = BasePage()

