Application URL to work with: http://automationpractice.com/

DESIGNED TEST SCENARIOS -->


test_1_positive:                Go to page
                                Sign in with registered user
                                Search Any course
                                Check searched course in found titles 

test_2_negative:                Go to page
                                Sign in with registered user
                                Search not existing course
                                Verify 'No Result Found' message is visible

TODO:                           pip install selenium webdriver
                                pip install pytest

Impotred Libraries:             webdriver_manager.chrome, selenium, selenium.webdriver.support,
                                selenium.webdriver.support.ui, selenium.webdriver.common.keys, 
                                selenium.webdriver.support.wait, selenium.webdriver.common.by,
                                string, random, logging, time ,pytest, json  

Design Pattern:                 Page Object Model (modular structure) 

Selector:                       XPATH

Project Modules:                conftest.py --> (includes driver initilisation method,
                                                includes methods 'logger' )

                            Helper -->                   
                                helpers.py  (includes all common methods which are used in 'Pages')
                                        Designed Methods: -->  

                                                'go_to_page'
                                                'find_and_click'
                                                'find_and_send_keys'
                                                'find' 
                                                'find_all'                             
                                                'waits'
                                                'wait_for_page'
                                                'random_str'                                       
                             
                                
                            Pages --> 
                                home_page.py
                                        Designed Methods: -->
                                                'click_sign_in'
                                                'click_sign_out'                                            
                                search_page.py 
                                        Designed Methods: -->
                                                'get_search_valid_name'
                                                'get_search_valid_name_all'
                                                'get_search_not_valid_name'                                             
                                sign_in_page.py
                                        Designed Methods: -->
                                                'login'
                                sign_up_page.py
                                         Designed Methods: -->
                                                'create_new_account'
                                                                                         
                            testdata -->
                                test_data.py (includes test data, which are used in tests)
                            cred.json (includes test data, which are used for signin)       
Test Cases:                               
                            tests: -->                               
                                'test_1_positive.py'
                                'test_2_negative.py'                                

Log                         test_log.txt
