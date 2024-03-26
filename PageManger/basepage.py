import time
import ddddocr
import requests
from PIL import Image
from Config.read_env import EnvironMent
from playwright.sync_api import *
import io
from Config.file_path import FilePath


class BasePage:

    def __init__(self):

        """with sync_playwright() as p:  不用with语句, 不用无头模式，将窗口最大化"""

        self.env = EnvironMent()
        p = sync_playwright().start()
        self.driver = p.chromium.launch(headless=False, args=['--start-maximized'])
        self.driver.context = self.driver.new_context(no_viewport=True)
        self.page = self.driver.context.new_page()
        self.login()
        time.sleep(3)

    def login(self):
        """登录"""

        # self.page.on('response', self.captcha_response)
        self.page.goto(self.env.url())
        self.page.locator('//input[@placeholder="账号"]').fill(self.env.account())
        self.page.locator('//input[@placeholder="密码"]').fill(self.env.password())
        self.page.locator('//img[@class="login-code-img"]').screenshot(path=FilePath.captcha_dir)
        captcha = self.ocr_captcha()
        self.page.locator('//input[@placeholder="验证码"]').fill(captcha)
        self.page.locator("//span[text()='登 录']").click()

    def gt_guide_page(self):
        """固投引导页 储备库列表"""
        self.page.locator("(//p[text()='储备库'])[1]").click()



    @staticmethod
    def get_captcha():
        """通过接口获取验证码"""
        res = requests.get(url='http://192.168.211.21:8088/ctrm/huanghe/login/captcha')
        ss = res.content
        return ss

    @staticmethod
    def ocr_captcha():
        """通过ocr识别接口数据"""
        ocr = ddddocr.DdddOcr()
        with open(FilePath.captcha_dir, 'rb') as f:
            img_bytes = f.read()

        img = Image.open(io.BytesIO(img_bytes))
        data = ocr.classification(img)
        return data

    def captcha_response(self, response):
        """获取验证码接口数据"""
        if '/login/captcha' in response.url:
            self.captcha_data = response.json()


if __name__ == '__main__':

    ad = BasePage()

