

from PageManger.CW_Page.Facility_Model.Facility import Facility


class TestFacility:

    @classmethod
    def setup_class(cls):

        cls.fa = Facility()

    def teardown_class(self):

        self.fa.page.close()

    def test_create_facility(self):

        assert_info = self.fa.create_facility()
        self.fa.assert_allure_screenshot(assert_info, True)
