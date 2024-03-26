

from PageManger.basepage import BasePage


class Facility(BasePage):

    def create_facility(self):
        """新增设施量"""

        self.page.locator("//p[text()='设施量清单']").click()
        self.page.locator("//span[text()='新增设施']").click()
        