import pytest
from playwright.sync_api import sync_playwright
from playwright.sync_api import Page
from config.config_parser import config





@pytest.fixture(scope="session")
def browser_type_launch_args(browser_type_launch_args):
    """Overrides default launch args with YAML values (REQ-007)"""
    return {
        **browser_type_launch_args,
        "headless": config.get_val("browser_settings.headless"),
        "slow_mo": config.get_val("browser_settings.slow_mo")
    }

@pytest.fixture
def check_config_type():
    """
    A setup fixture that returns a helper function 
    to inspect YAML value types.
    """
    def _get_type(key_path):
        # Retrieve the value using our parser
        value = config.get_val(key_path)
        
        if value is None:
            return f"Key '{key_path}' not found in YAML."
        
        # Return the Python type name
        return type(value).__name__
    
    return _get_type

@pytest.fixture(scope="function")
def set_up(page):
    # This 'page' fixture is provided by pytest-playwright automatically
    page.set_viewport_size({"width": 1920, "height": 1080})
    yield page
    # Teardown: Playwright handles closing context/page automatically


#Im writing a fixture to get url using getoption before every test runs
@pytest.fixture(scope="session")
def get_my_url_from_cmd(request):
    return request.config.getoption("--baseurl")

@pytest.fixture(scope="function",autouse=True)
def launch_app(page:Page,get_my_url_from_cmd:str):
    page.goto(get_my_url_from_cmd,wait_until="domcontentloaded")

    yield page

    print("test completion is done this is teardown")


def pytest_addoption(parser):
    parser.addoption(
        "--baseurl", 
        action="store", 
        default="https://myacl.acldigital.com/",
        help="The URL of the application under test"
    )


