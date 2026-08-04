import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MainPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step("Добавить Backpack в корзину")
    def add_backpack(self) -> None:
        """Добавляет Sauce Labs Backpack в корзину."""
        self.wait.until(
            EC.presence_of_element_located((By.CLASS_NAME, "inventory_list"))
        )
        self.driver.find_element(
            By.XPATH,
            "//button[@data-test='add-to-cart-sauce-labs-backpack']"
        ).click()

    @allure.step("Добавить Bolt T-Shirt в корзину")
    def add_bolt_tshirt(self) -> None:
        """Добавляет Sauce Labs Bolt T-Shirt в корзину."""
        self.driver.find_element(
            By.XPATH,
            "//button[@data-test='add-to-cart-sauce-labs-bolt-t-shirt']"
        ).click()

    @allure.step("Добавить Onesie в корзину")
    def add_onesie(self) -> None:
        """Добавляет Sauce Labs Onesie в корзину."""
        self.driver.find_element(
            By.XPATH,
            "//button[@data-test='add-to-cart-sauce-labs-onesie']"
        ).click()

    @allure.step("Перейти в корзину")
    def go_to_cart(self) -> None:
        """Переходит на страницу корзины."""
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
