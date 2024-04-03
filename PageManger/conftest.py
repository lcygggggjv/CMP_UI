
import pytest
from hamcrest import assert_that, equal_to
from playwright.sync_api import sync_playwright

from Config.file_path import FilePath
from PageManger.basepage import BasePage


@pytest.fixture(scope="module")
def setup_page():

    p = sync_playwright().start()
    browser = p.chromium.launch(headless=False, args=['--start-maximized'])
    context = browser.new_context(no_viewport=True)
    page = context.new_page()

    yield page
