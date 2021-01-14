from selenium import webdriver
from Misc_Methods.get_path import GetPath
from selenium.webdriver.chrome.options import Options
from Misc_Methods.read_config import ReadConfig


def get_browser():
    options = Options()
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    driver = webdriver.Chrome(executable_path=GetPath().get_driver(), chrome_options=options)
    driver.maximize_window()
    driver.implicitly_wait(30)
    driver.get(ReadConfig().get_url())


