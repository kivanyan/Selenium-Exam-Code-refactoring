from Helper import helpers
from Testdata import test_data # TODO not used
from Pages import sign_in_page, sign_up_page, search_page
from conftest import logger
import config as data


def test_search_not_valid_name(driver):
    helpers.go_to_page(driver, data.main_url)
    sign_in_page.login(driver)
    result_not_valid = search_page.get_search_not_valid_name(driver)
    assert search_page.msg_not_result, logger("Failed")
    logger("'No Result Found' message is visible")
