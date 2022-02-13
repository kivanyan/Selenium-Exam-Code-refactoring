from selenium.webdriver.common.by import By
from Helper import helpers
from Pages import home_page, sign_up_page
from Testdata import test_data
from conftest import logger
import json


txt_email = (By.XPATH, "//input[@id='user[email]']")
txt_pass = (By.XPATH, "//input[@id='user[password]']")
check_remember_me = (By.XPATH, "//input[@id='user[remember_me]']")
btn_login = (By.XPATH, "//input[@class='button button-primary g-recaptcha']")


def login(driver, email="", password=""):
    with open('cred.json') as file:
        data = json.load(file)
        if data["email"] == '' or data["password"] == '':
            sign_up_page.create_new_account(driver)
        else:
            home_page.click_sign_in(driver)
            logger(f"Login with email and password: [{data['email']} : {data['password']}]")
            helpers.find_and_send_keys(driver, txt_email, data["email"])
            helpers.find_and_send_keys(driver, txt_pass, data["password"])
            helpers.find_and_click(driver, check_remember_me)
            helpers.find_and_click(driver, btn_login)
            helpers.wait_for_page(driver, "/collections")
            logger("Sign in successfully!")
