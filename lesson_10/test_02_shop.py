
import allure
from selenium import webdriver
from login_page import LoginPage
from main_page import MainPage
from cart_page import CartPage
from checkout_page import CheckoutPage


@allure.title("Проверка покупки трёх товаров в магазине")
@allure.description(
    "Тест проверяет что итоговая сумма покупки "
    "Backpack + Bolt T-Shirt + Onesie равна $58.29"
)
@allure.feature("Интернет-магазин")
@allure.severity(allure.severity_level.CRITICAL)
def test_shop():
    driver = webdriver.Firefox()

    with allure.step("Открыть магазин и авторизоваться"):
        login = LoginPage(driver)
        login.open()
        login.login("standard_user", "secret_sauce")

    with allure.step("Добавить товары в корзину"):
        main = MainPage(driver)
        main.add_backpack()
        main.add_bolt_tshirt()
        main.add_onesie()
        main.go_to_cart()

    with allure.step("Перейти к оформлению заказа"):
        cart = CartPage(driver)
        cart.checkout()

    with allure.step("Заполнить форму и получить итоговую сумму"):
        checkout = CheckoutPage(driver)
        checkout.fill_form("Владислав", "Веденеев", "630001")
        total = checkout.get_total()

    driver.quit()

    with allure.step("Проверить итоговую сумму"):
        assert total == "Total: $58.29"
