import time

from Pages.home_page import HomePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException


class HomeObjects:
    def __init__(self, driver):
        self.driver = driver

    def enter_value_on_search_field(self, value):
        HomePage(self.driver).search_field().click()
        HomePage(self.driver).search_field().send_keys(value)
        HomePage(self.driver).search_field().send_keys(Keys.ENTER)

    def click_on_accept_cookies_button(self):
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID,
                                                                                   'onetrust-accept-btn-handler')))
            HomePage(self.driver).accept_cookies_button().click()
        except NoSuchElementException:
            return None

    def check_products_appearing(self, letter):
        WebDriverWait(self.driver, 10).until(EC.url_contains, letter)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//div[contains(@class, '
                                                                                         '"GenericProduct__StyledProductLayout-sc-6ow56k-2 dRrPqt")]')))
        data = HomePage(self.driver).select_first_record().is_displayed()
        return data

    def select_wishlist_button(self):
        HomePage(self.driver).select_heart_button().click()

    def get_wishlist_count(self):
        WebDriverWait(self.driver, 10).until(EC.invisibility_of_element_located((By.XPATH, '//div[contains(@class, '
                                                                                           '"ScrollableArea__StyledScrollableContainer-v545jt-0 kVDQL")]')))
        return HomePage(self.driver).wishlist_count().text

    def click_on_wishlist_link(self):
        HomePage(self.driver).wishlist_link().click()
