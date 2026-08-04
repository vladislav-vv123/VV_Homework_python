import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step("Заполнить форму: {first_name} {last_name} {postal_code}")
    def fill_form(
        self,
        first_name: str,
        last_name: str,
        postal_code: str
    ) -> None:
        """Заполняет форму оформления заказа.

        Args:
            first_name: имя покупателя
            last_name: фамилия покупателя
            postal_code: почтовый индекс
        """
        self.driver.find_element(By.ID, "first-name").send_keys(first_name)
        self.driver.find_element(By.ID, "last-name").send_keys(last_name)
        self.driver.find_element(By.ID, "postal-code").send_keys(postal_code)
        self.driver.find_element(By.ID, "continue").click()

    @allure.step("Получить итоговую стоимость")
    def get_total(self) -> str:
        """Возвращает итоговую стоимость заказа.

        Returns:
            Строка с итоговой стоимостью
        """
        self.wait.until(
            EC.presence_of_element_located(
                (By.CLASS_NAME, "summary_total_label")
            )
        )
        return self.driver.find_element(
            By.CLASS_NAME, "summary_total_label"
        ).text
