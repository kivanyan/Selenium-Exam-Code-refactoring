from selenium.webdriver.common.by import By
from Helper import helpers
from conftest import logger
import pytest


btn_signin = (By.XPATH, "//section[@class='header__user-menu']//a[contains(text(), 'Sign In')]")
btn_logout = (By.XPATH, "//img[@class='header__user-avatar']")
btn_signout = (By.XPATH, "//li[@class='dropdown__menu-item']//a[contains(text(), 'Sign Out')]")


def click_sign_in(driver):
    logger("Sign in")
    helpers.find_and_click(driver, btn_signin)
    helpers.wait_for_page("/sign_in")


def click_sign_out(driver):
    logger("Logout")
    helpers.find_and_click(driver, btn_logout)
    helpers.find(driver, btn_signout)
