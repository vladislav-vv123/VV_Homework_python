from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MainPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def add_backpack(self):
        self.wait.until(
            EC.presence_of_element_located((By.CLASS_NAME, "inventory_list"))
        )
        self.driver.find_element(
            By.XPATH,
            "//button[@data-test='add-to-cart-sauce-labs-backpack']"
        ).click()

    def add_bolt_tshirt(self):
        self.driver.find_element(
            By.XPATH,
            "//button[@data-test='add-to-cart-sauce-labs-bolt-t-shirt']"
        ).click()

    def add_onesie(self):
        self.driver.find_element(
            By.XPATH,
            "//button[@data-test='add-to-cart-sauce-labs-onesie']"
        ).click()

    def go_to_cart(self):
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
