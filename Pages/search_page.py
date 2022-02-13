import time
from conftest import logger
from Helper import helpers
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from Pages import home_page, sign_up_page
from Testdata import test_data


search_field = (By.XPATH, "//input[@name='q']")
ultimate_img = (By.XPATH, "//a/img[@title='Ultimate QA']")
aria_label = (By.XPATH, "//a[@aria-label='Next page']")
search_all = (By.XPATH, "//div[@class='course-card__body']/h3")
search_result = (By.XPATH, f"//h3[contains(text(),'{test_data.search_valid_name}')]")
msg_not_result = (By.XPATH, "//p[@class='products__list-no-results']")


def get_search_valid_name(driver):

    helpers.find_and_send_keys(driver, search_field, (test_data.search_valid_name, Keys.ENTER))
    time.sleep(10)
    item_text_list = []
    result_all = helpers.find_all(driver, search_all)
    page_items = get_page_item_count(driver)
    assert page_items > 0
    for item in result_all:
        (item_text_list.append(item.text))    
    while len(helpers.find_all(driver, aria_label)) > 0:
        helpers.find_and_click(driver, aria_label)
        result_all = helpers.find_all(driver, search_all)
        for item in result_all:
            (item_text_list.append(item.text))
        s_titles = [title for title in item_text_list]
        return s_titles


def get_search_not_valid_name(driver):
    helpers.find_and_send_keys(driver, search_field, (test_data.search_not_valid_name, Keys.ENTER))


def get_page_item_count(driver):
    page_items = len(helpers.find_all(driver, search_all))
    return page_items



