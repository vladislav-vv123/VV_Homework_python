import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step("Нажать кнопку Checkout")
    def checkout(self) -> None:
        """Нажимает кнопку перехода к оформлению заказа."""
        self.wait.until(
            EC.presence_of_element_located((By.ID, "checkout"))
        )
        self.driver.find_element(By.ID, "checkout").click()
