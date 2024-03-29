import time

from Utils.Mock import Mock
from PageManger.basepage import BasePage


class Facility(BasePage):

    mock = Mock()

    def create_facility(self):
        """新增设施量"""

        self.page.locator("//p[text()='设施量清单']").click()
        self.page.locator("//span[text()='新增设施']").click()
        self.page.locator("//label[text()='设施名称:']/following-sibling::div//input").fill(self.mock.rand_str())
        self.page.locator("//label[text()='设施类型:']/following-sibling::div//input").click()
        self.page.locator("//li[text()='公路']").click()
        self.page.locator("//label[text()='地理位置:']/following-sibling::div//input").fill("上海市嘉定区嘉定镇")
        self.page.locator("//label[text()='建成时间:']/following-sibling::div//input").click()
        self.page.locator("(//span[text()='13'])[1]").click()
        self.page.locator("//label[text()='最后中修时间:']/following-sibling::div//input").click()
        self.page.locator("(//span[text()='13'])[2]").click()
        self.page.locator("//label[text()='最后大修时间:']/following-sibling::div//input").click()
        self.page.locator("(//span[text()='13'])[3]").click()
        self.page.locator("//label[text()='设施状态:']/following-sibling::div//input").click()
        self.page.locator("//li[text()='待大修']").click()
        self.page.locator("//label[text()='中修维护周期:']/following-sibling::div//input").fill('24')
        self.page.locator("//label[text()='大修维护周期:']/following-sibling::div//input").fill('36')
        self.page.locator("//span[text()='确认']").click()
        self.page.locator("(//span[text()='确定'])[4]").click()
        actual_info = self.page.locator("//p[text()='处理成功']").is_visible()
        return actual_info

