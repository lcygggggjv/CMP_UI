import logging
import sys
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
        actual_info = self.loop_assert("//p[text()='处理成功']")
        return actual_info

    # def test_create_facility(self):
    #     """新增设施量"""
    #
    #     setup_page.page.locator("//p[text()='设施量清单']").click()
    #     setup_page.page.locator("//span[text()='新增设施']").click()
    #     setup_page.page.locator("//label[text()='设施名称:']/following-sibling::div//input").fill(self.mock.rand_str())
    #     setup_page.page.locator("//label[text()='设施类型:']/following-sibling::div//input").click()
    #     setup_page.page.locator("//li[text()='公路']").click()
    #     setup_page.page.locator("//label[text()='地理位置:']/following-sibling::div//input").fill("上海市嘉定区嘉定镇")
    #     setup_page.page.locator("//label[text()='建成时间:']/following-sibling::div//input").click()
    #     setup_page.page.locator("(//span[text()='13'])[1]").click()
    #     setup_page.page.locator("//label[text()='最后中修时间:']/following-sibling::div//input").click()
    #     setup_page.page.locator("(//span[text()='13'])[2]").click()
    #     setup_page.page.locator("//label[text()='最后大修时间:']/following-sibling::div//input").click()
    #     setup_page.page.locator("(//span[text()='13'])[3]").click()
    #     setup_page.page.locator("//label[text()='设施状态:']/following-sibling::div//input").click()
    #     setup_page.page.locator("//li[text()='待大修']").click()
    #     setup_page.page.locator("//label[text()='中修维护周期:']/following-sibling::div//input").fill('24')
    #     setup_page.page.locator("//label[text()='大修维护周期:']/following-sibling::div//input").fill('36')
    #     setup_page.page.locator("//span[text()='确认']").click()
    #     setup_page.page.locator("(//span[text()='确定'])[4]").click()
    #     # actual_info = setup_page.page.locator("//p[text()='处理成功']").is_visible()
    #     # # setup_page.assert_allure_screenshot(actual_info, True)
    #     for i in range(3):
    #         actual_info = setup_page.page.locator("//p[text()='处理成功']").is_visible()
    #         print(f"这是实际{actual_info}, 第{i}次")
    #         if actual_info:
    #             setup_page.assert_allure_screenshot(actual_info, True)
    #             break
    #         time.sleep(1)

    def create_required(self):
        """新增必填"""

        self.page.locator("//button//span[text()='新增设施']").click()
        self.page.locator("//span[text()='确认']").click()
        count_list = self.loop_find_locator_two("//div[text()='请选择']", "//div[text()='请输入']")
        print(count_list[0], count_list[1])
        return count_list[0], count_list[1]

    def export_file(self):
        """导出附件"""

        self.page.locator("//p[text()='设施量清单']").click()
        self.page.locator("(//span[@class='el-checkbox__inner'])[2]").click()
        self.page.locator("//span[text()='导出']").click()
        self.page.locator("//button//span[text()='确定']").click()



