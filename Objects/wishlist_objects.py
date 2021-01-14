from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Pages.wishlist_page import WishlistPage
from Misc_Methods.get_path import GetPath
import os


class WishlistObjects:
    def __init__(self, driver):
        self.driver = driver

    def get_current_url(self):
        return self.driver.current_url

    def wait_till_url_contains(self, text):
        WebDriverWait(self.driver, 10).until(EC.url_contains, text)

    def click_on_delete_wishlist_button(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="wishlistRoot"]//li'
                                                                                         '/button')))
        WishlistPage(self.driver).delete_wishlist_button().click()

    def save_screenshot(self):
        WebDriverWait(self.driver, 10).until(EC.invisibility_of_element_located((By.XPATH, '//*[@id="wishlistRoot"]//li'
                                                                                           '/button')))
        image_path = GetPath().save_screenshot('image.png')
        if os.path.exists(image_path):
            os.remove(image_path)
            self.driver.save_screenshot(image_path)
        else:
            self.driver.save_screenshot(image_path)
