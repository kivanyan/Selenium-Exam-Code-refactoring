from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from Helper import helpers
from conftest import logger
from Pages import home_page
import json



btn_create_account = (By.XPATH, "//a[contains(text(),'Create a new account')]")
txt_first_name = (By.XPATH, "//input[@id='user[first_name]']")
txt_last_name = (By.XPATH, "//input[@id='user[last_name]']")
txt_email = (By.XPATH, "//input[@id='user[email]']")
txt_pass = (By.XPATH, "//input[@id='user[password]']")
input_chekcbox = (By.XPATH, "//input[@id='user[terms]']")
btn_submit_registration = (By.XPATH, "//input[@value='Sign up']")



def create_new_account(driver, new_email="", new_pass=""):
    home_page.click_sign_in(driver)    
    helpers.find_and_click(driver, btn_create_account)

    firstname = helpers.random_str(driver, 6, True, False)
    lastname = helpers.random_str(driver, 6, True, False)
    new_email = new_email if new_email else f"{helpers.random_str(driver, 10, True, True)}@{helpers.random_str(driver, 5,True, True)}.com"
    new_pass = new_pass if new_pass else helpers.random_str(driver, 10,True, True)

    helpers.find_and_send_keys(driver, txt_first_name, firstname)
    helpers.find_and_send_keys(driver, txt_last_name, lastname)
    helpers.find_and_send_keys(driver, txt_email, new_email)
    helpers.find_and_send_keys(driver, txt_pass, new_pass)


    with open('cred.json') as file:
        data = json.load(file)
        data["email"] = new_email
        data["password"] = new_pass
    with open('cred.json', 'w') as file:
        json.dump(data, file)
    helpers.find_and_click(driver, input_chekcbox)
    helpers.find_and_click(driver, btn_submit_registration)     
    helpers.wait_for_page(driver, "/collections")
    logger("Registered successfully!")
    return new_email, new_pass
