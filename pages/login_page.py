from pages.base_page import BasePage
from playwright.sync_api import expect

class LoginPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self._username = "input[name='username']"
        self._password = "input[name='password']"
        self._login_btn = page.get_by_role("button",name="Sign In")

        self.acl_username=page.get_by_role("textbox",name="Username")
        self.acl_password=page.get_by_role("textbox",name="Password")
        self.acl_sign_in_button=page.get_by_role('button',name='Sign In')
        self._iframe_locator="#mce_0_ifr"
        self.acl_logo=page.get_by_role('img',name="logo")
        self.my_apps_link=page.locator('li.dropdown').locator('a.icon').locator('img.icon-img').nth(7)
        self.lms_link=page.get_by_text("Learning Management System",exact=False)


    def login(self, user, pwd):
        # self.fill_text(self._username, user)
        # self.fill_text(self._password, pwd)
        # self._login_btn.click()

        iframe=self.get_iframe(self._iframe_locator)
        element_in_iframe=iframe.get_by_text('Your content goes here.')
        expect(element_in_iframe).to_be_visible()
    
    def login_to_acl(self,user,pwd):
        self.fill_text(self.acl_username, user)
        self.fill_text(self.acl_password, pwd)
        self.acl_sign_in_button.click()
        expect(self.acl_logo).to_be_visible(timeout=50000)

    def navigate_to_lms(self):
        expect(self.my_apps_link).to_be_visible()
        self.my_apps_link.hover()
        
        with self.page.context.expect_page() as new_page_info:
            self.lms_link.click()

    
        #2. Get the new page object
        new_page = new_page_info.value
        new_page.wait_for_load_state()
        return new_page
    
