from selenium import webdriver
from login_page import LoginPage
from main_page import MainPage
from cart_page import CartPage
from checkout_page import CheckoutPage


def test_shop():
    driver = webdriver.Firefox()

    login = LoginPage(driver)
    login.open()
    login.login("standard_user", "secret_sauce")

    main = MainPage(driver)
    main.add_backpack()
    main.add_bolt_tshirt()
    main.add_onesie()
    main.go_to_cart()

    cart = CartPage(driver)
    cart.checkout()

    checkout = CheckoutPage(driver)
    checkout.fill_form("Владислав", "Веденеев", "630001")
    total = checkout.get_total()

    driver.quit()

    assert total == "Total: $58.29"
