Feature: Basic Flow of Cart and Wishlist
  Scenario: Check App should display the results as per desired request
    When Search for "möbel"
    Then App should display product listing page with a list of products
  Scenario: Check Login/Registration Overlay display on Clicking Wishlist Icon
    When Click on wishlist icon of the first found product
    Then App should see the login/registration overlay
  Scenario: Check that App should add product to Wishlist after successful login
    When Switch to login form of the overlay
    And Log in with valid credentials
    Then The Product should be added to the wishlist (wishlist icon on the product is filled in and wishlist counter in the website header shows 1)
  Scenario: Check That App should remove that product from Wishlist when clicked on Cross Button
    When Click on Wishlist Link Button
    Then App should navigate to the wishlist page
    And App should delete the product from my wishlist and Take Screenshot