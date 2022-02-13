from Helper import helpers
from Testdata import test_data
from Pages import sign_in_page, sign_up_page, search_page
from conftest import logger
import config as data


def test_search_valid_name(driver):
    helpers.go_to_page(driver, data.main_url)
    sign_in_page.login(driver)
    search_result = search_page.get_search_valid_name(driver)
    assert {test_data.search_valid_name} in search_result, logger("Search course not found in some titles")   
