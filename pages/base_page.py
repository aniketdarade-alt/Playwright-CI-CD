from playwright.sync_api import Page, Response
from playwright.sync_api import expect

class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def navigate(self, url: str) -> Response | None:
        return self.page.goto(url, wait_until="networkidle")

    def click(self, selector: str):
        self.page.wait_for_selector(selector)
        self.page.click(selector)

    def fill_text(self, selector, text: str):
    
        if(isinstance(selector,str)):    
            required_selector=self.page.locator(selector)
            required_selector.press_sequentially(text,delay=100)
        else:
            selector.press_sequentially(text,delay=100)

    def get_iframe(self,selector:str):
        iframe=self.page.frame_locator(selector)
        return iframe
    
    def get_attribute(self,selector,attribute_name):
        if(isinstance(selector,str)):
            attribute=self.page.locator(selector).get_attribute(attribute_name)
        else:
            attribute=selector.get_attribute(attribute_name)

        return attribute
    
    def validate_text_inside_element(self,selector,expected_text):

        if(isinstance(selector,str)):
            element=self.page.locator(selector)
            expect(element).to_contain_text(expected_text)

        else:
            expect(selector).to_contain_text(expected_text)

    def validate_text_displayed_on_page(self,text:str,timeout:int=50000):

        try:
            expect(self.page.locator("body")).to_contain_text(text,timeout=timeout)
            return True
        except AssertionError:
            return False
