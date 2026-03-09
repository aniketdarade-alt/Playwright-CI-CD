from pages.login_page import LoginPage
from playwright.sync_api import expect
import logging
import pytest


def test_valid_login(page):
    login_page = LoginPage(page)
    
    # login_page.navigate("https://myacl.acldigital.com/")
    login_page.navigate("https://the-internet.herokuapp.com/iframe")
    login_page.login("aniket.darade", "Uzumakinaruto@1")
    
    # Industry standard: Use 'expect' for auto-retrying assertions
    # expect(page).to_have_url("https://example.com/dashboard")
    print(page.url)

@pytest.mark.window
def test_window(page):
    login_page=LoginPage(page)
    login_page.login_to_acl("aniket.darade","Uzumakinaruto@1")
    new_page=login_page.navigate_to_lms()
    new_page=LoginPage(new_page)

@pytest.mark.window2
def test_verify_config_types(check_config_type):
    # Check a string value
    assert check_config_type("env_variables.base_url") == "str"
    print(check_config_type("viewports.desktop.width"))
    
    # Check a number value
    assert check_config_type("browser_settings.timeout") == "int"
    
    # Check a boolean value
    assert check_config_type("browser_settings.headless") == "bool"
    
    # Check a nested dictionary (map)
    assert check_config_type("viewports.desktop") == "dict"
    
    
    # with page.context.expect_page() as new_page_info:
    #     page.get_by_text("Open New Window").click() # Link with target="_blank"
    
    # # 2. Get the new page object
    # new_page = new_page_info.value
    
    # # 3. Interact with the new window directly
    # new_page.wait_for_load_state()
    # print(f"New Window URL: {new_page.url}")
    # new_page.get_by_role("button", name="Submit").click()
    
    # page.bring_to_front() # Optional: brings the tab into view
    # page.get_by_role("link", name="Logout").click()