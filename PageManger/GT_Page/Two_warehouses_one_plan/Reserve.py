

from PageManger.basepage import BasePage


class Reserve(BasePage):

    def create_reserve(self):
        """新增储备库"""

        self.gt_guide_page()
        self.page.locator("//span[text()='项目申报']").click()
