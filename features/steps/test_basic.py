from Misc_Methods.read_config import ReadConfig
from Objects.home_objects import HomeObjects
from behave import *
from Objects.login_objects import LoginObjects
from Objects.wishlist_objects import WishlistObjects


@when(u'Search for "möbel"')
def step_impl(context):
    value_to_search = ReadConfig().search_text()
    HomeObjects.enter_value_on_search_field(context, value_to_search)


@then(u'App should display product listing page with a list of products')
def step_impl(context):
    value_to_search = ReadConfig().search_text()
    assert (HomeObjects.check_products_appearing(context, value_to_search) is True)


@when(u'Click on wishlist icon of the first found product')
def step_impl(context):
    HomeObjects.select_wishlist_button(context)


@then(u'App should see the login/registration overlay')
def step_impl(context):
    assert (LoginObjects.check_login_page_displayed(context) is True)


@when(u'Switch to login form of the overlay')
def step_impl(context):
    email = ReadConfig().get_user_email()
    password = ReadConfig().get_user_email_password()
    LoginObjects.enter_email(context, email)
    LoginObjects.enter_password(context, password)


@when(u'Log in with valid credentials')
def step_impl(context):
    LoginObjects.check_accept_agreement_checkbox(context)
    LoginObjects.login_user(context)


@then(u'The Product should be added to the wishlist (wishlist icon on the product is filled in and wishlist counter '
      u'in the website header shows 1)')
def step_impl(context):
    assert (HomeObjects.get_wishlist_count(context) == str(1))


@when(u'Click on Wishlist Link Button')
def step_impl(context):
    HomeObjects.click_on_wishlist_link(context)


@then(u'App should navigate to the wishlist page')
def step_impl(context):
    wishlist_url = ReadConfig().get_wishlist_url()
    WishlistObjects.wait_till_url_contains(context, 'wishlist')
    assert (WishlistObjects.get_current_url(context) == wishlist_url)


@then(u'App should delete the product from my wishlist and Take Screenshot')
def step_impl(context):
    WishlistObjects.click_on_delete_wishlist_button(context)
    WishlistObjects.save_screenshot(context)

