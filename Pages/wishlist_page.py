class WishlistPage:
    def __init__(self, driver):
        super().__init__()
        self.driver = driver

    def delete_wishlist_button(self):
        return self.driver.find_element_by_xpath('//*[@id="wishlistRoot"]//li/button')
