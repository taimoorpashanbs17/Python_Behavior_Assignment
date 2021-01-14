from behave import fixture, use_fixture
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from Misc_Methods.get_path import GetPath
from selenium.common.exceptions import InvalidSessionIdException

from Misc_Methods.read_config import ReadConfig


@fixture
def selenium_browser_chrome(context):
    options = Options()
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    options.add_argument("user-data-dir="+GetPath().get_chrome_profile())
    context.driver = webdriver.Chrome(GetPath().get_driver(), chrome_options=options)
    context.driver.maximize_window()
    context.driver.implicitly_wait(30)
    context.driver.get(ReadConfig().get_url())
    yield context.driver


@fixture
def close_browser(context):
    context.driver.close()


def before_feature(context, feature):
    use_fixture(selenium_browser_chrome, context)


def after_feature(context, feature):
    try:
        use_fixture(close_browser, context)
    except InvalidSessionIdException:
        return None
