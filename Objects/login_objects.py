from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Pages.login_page import LoginPage
from selenium.webdriver.common.keys import Keys


class LoginObjects:
    def __init__(self, driver):
        self.driver = driver

    def check_login_page_displayed(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//div[contains(@class, '
                                                                                         '"ScrollableArea__StyledScrollableContainer-v545jt-0 kVDQL")]')))
        data = LoginPage(self.driver).login_form().is_displayed()
        return data

    def enter_email(self, email):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.NAME, 'email')))
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.NAME, 'email')))
        LoginPage(self.driver).email_field().click()
        LoginPage(self.driver).email_field().send_keys(email)

    def enter_password(self, password):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.NAME, 'password')))
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.NAME, 'password')))
        LoginPage(self.driver).password_field().click()
        LoginPage(self.driver).password_field().send_keys(password)

    def check_accept_agreement_checkbox(self):
        LoginPage(self.driver).accepting_terms_checkbox().click()

    def login_user(self):
        LoginPage(self.driver).password_field().send_keys(Keys.ENTER)
