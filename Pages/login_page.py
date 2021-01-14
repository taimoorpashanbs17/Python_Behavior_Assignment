class LoginPage:
    def __init__(self, driver):
        super().__init__()
        self.driver = driver

    def login_form(self):
        return self.driver.find_element_by_xpath('//div[contains(@class, "ScrollableArea__StyledScrollableContainer'
                                                 '-v545jt-0 '
                                                 'kVDQL")]')

    def email_field(self):
        return self.driver.find_element_by_name('email')

    def password_field(self):
        return self.driver.find_element_by_name('password')

    def accepting_terms_checkbox(self):
        return self.driver.find_element_by_name('isTermsAccepted')
