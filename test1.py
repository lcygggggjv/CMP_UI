


# class bas:
#
#
#     @staticmethod
#     def a():
#
#         print("这是实例方法")


# print(bas.a)

# def hello():
#
#     print("这是")
#
#
# def hc(function):
#
#     function()
#
# hc(hello)


import asyncio

from playwright.async_api import async_playwright
from playwright.sync_api import sync_playwright, expect
from Config.read_env import EnvironMent


class BasePage:
    # ... 其他代码 ...

    async def login(self):
        """登录"""

        self.env = EnvironMent()
        async with async_playwright() as p:

            self.driver = await p.chromium.launch(headless=False, args=['--start-maximized'])
            self.driver.context = await self.driver.new_context(no_viewport=True)
            self.page = await self.driver.context.new_page()
            self.page.on('response', self.captcha_response)
            await self.page.goto(self.env.url())
            await self.page.locator('//input[@placeholder="账号"]').fill(self.env.account())
            await self.page.locator('//input[@placeholder="密码"]').fill(self.env.password())
        # 这里可能需要一些逻辑来提交表单或触发验证码的发送
        # 例如，点击登录按钮等

        # 假设你有一个方法来处理验证码输入（这通常是手动或通过OCR等方式）
        # self.handle_captcha()

        # 这里你可以添加一个等待条件，确保 captcha_data 被设置
        # 例如，等待某个元素出现，或者根据具体的业务逻辑来等待
        # 注意：这只是一个示例，你需要根据你的实际业务逻辑来编写等待条件
        # expect(self.page).to_have_attribute('value', 'some_expected_value')

    def captcha_response(self, response):
        """获取验证码接口数据"""
        if '/login/captcha' in response.url:
            self.captcha_data = response.content
            # 可以在这里添加逻辑来处理验证码数据，例如打印出来或保存到文件等
            print("Captcha data received:", self.captcha_data)

            # ... 可能还需要其他方法来处理登录后的操作 ...


# 在主函数中，你需要使用异步的方式来调用 BasePage 的方法
async def main():
    ad = BasePage()
    # 假设 login 方法现在是异步的，并且它处理完登录和验证码后返回
    await ad.login()
    # 现在可以安全地访问 captcha_data，因为它已经在 login 方法中被设置了
    print(ad.captcha_data)


# 使用 asyncio 运行主函数
asyncio.run(main())


