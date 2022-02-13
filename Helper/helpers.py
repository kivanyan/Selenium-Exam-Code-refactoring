import random
import string
from conftest import logger

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.action_chains import ActionChains # TODO not used


def go_to_page(driver, url, new_window=False):
    if new_window:
        driver.execute_script(f"window.open('{url}');")
    else:
        driver.get(url)
        driver.maximize_window()


def find_and_click(driver, loc, timeout=3):
    try:
        elem = find(driver, loc, timeout)
        elem.click()
        logger("The element was successfully found and clicked")
    except Exception as e:
        logger(e, True)



def find_and_send_keys(driver, loc, inp_text, timeout=10):
    try:
        elem = find(driver, loc, timeout)
        elem.send_keys(inp_text)
        logger("The data was successfully sent")
    except Exception as e:
        logger(e, True)


def find(driver, loc, timeout=20, should_exist=True, get_text="", get_attribute=""):
    try:
        elem = WebDriverWait(driver, timeout).until(expected_conditions.presence_of_element_located(loc),
                                                    message=f"Element '{loc}' not found!")
    except Exception as e:
        # logger(e, error=True)
        if should_exist:
            raise Exception(e)
        return False
    if get_text:
        return elem.text
    elif get_attribute:
        return elem.get_attribute(get_attribute)
    return elem    



def find_all(driver, loc, timeout=10):
    try:
        elements = WebDriverWait(driver, timeout).until(expected_conditions.presence_of_all_elements_located(loc),
                                                        message=f"Elements '{loc}' not found!")
    except Exception as e:
        logger(e, error=True)         
        return False
    return elements


def waits(driver, loc, timeout=10, wait_type=""):
    if wait_type == "presence":
        WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located(loc), message=f"Element '{loc}' not found")
    elif wait_type == "all_presence":
        WebDriverWait(driver, timeout).until(EC.presence_of_all_elements_located(loc),
                                             message=f"Elements '{loc}' not found!")
    elif wait_type == "visibility":
        WebDriverWait(driver, timeout).until(
            EC.visibility_of_element_located(loc),
            message=f"Elements '{loc}' not found!")
    elif wait_type == "invisibility":
        WebDriverWait(driver, loc).until(EC.invisibility_of_element_located(loc),
                                         message=f"Element '{loc}' not found")
    elif wait_type == "clickable":
        WebDriverWait(driver, timeout).until(
            EC.element_to_be_clickable(loc),
            message=f"Elements '{loc}' not found!")
    elif wait_type == "selected":
        WebDriverWait(driver, timeout).until(
            EC.element_to_be_selected(loc),
            message=f"Elements '{loc}' not found!")
    else:
        logger("Type of wait is incorrect!")


def wait_for_page(driver, page="", not_page="", timeout=10):
    if page:
        WebDriverWait(driver, timeout).until(expected_conditions.url_contains(page))
    elif not_page:
        WebDriverWait(driver, timeout).until_not(expected_conditions.url_contains(not_page))


def random_str(driver, symbols_count, letters=True, digits=True):
    if letters and digits:
        return ''.join(random.choices(string.ascii_letters + string.digits, k=symbols_count))
    elif letters:
        return ''.join(random.choices(string.ascii_letters, k=symbols_count))
    else:
        return ''.join(random.choices(string.digits, k=symbols_count))


