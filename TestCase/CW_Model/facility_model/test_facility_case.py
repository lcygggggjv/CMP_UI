
import time

import pytest

from PageManger.CW_Page.Facility_Model.Facility import Facility


class TestFacility:

    @classmethod
    def setup_class(cls):

        cls.fa = Facility()

    def test_create_facility(self):

        assert_info = self.fa.create_facility()
        self.fa.assert_allure_screenshot(assert_info, True)

    def test_create_required(self):

        assert_info = self.fa.create_required()
        self.fa.assert_allure_screenshot(len(assert_info[0]), 5)
        self.fa.assert_allure_screenshot(len(assert_info[1]), 2)
