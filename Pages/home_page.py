class HomePage:
    def __init__(self, driver):
        super().__init__()
        self.driver = driver

    def search_field(self):
        return self.driver.find_element_by_tag_name("input")

    def accept_cookies_button(self):
        return self.driver.find_element_by_id("onetrust-accept-btn-handler")

    def displaying_records(self):
        return self.driver.find_elements_by_xpath(
            '//div[contains(@class, "GenericProduct__StyledProductLayout-sc-6ow56k-2 dRrPqt")]')

    def select_first_record(self):
        return HomePage(self.driver).displaying_records()[0]

    def select_heart_button(self):
        return self.driver.find_element_by_xpath('//*[@id="app-root"]//div[1]/a/div/div[2]/div[2]/div')

    def wishlist_link(self):
        return self.driver.find_element_by_xpath('//*[@id="wwOneHeader"]//div[3]/div/span[2]')

    def wishlist_count(self):
        return self.driver.find_element_by_xpath('//*[@id="wwOneHeader"]//div/span[1]/span')
