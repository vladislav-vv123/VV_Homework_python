import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 60)

    @allure.step("Открыть страницу калькулятора")
    def open(self) -> None:
        """Открывает страницу калькулятора."""
        url = "https://bonigarcia.dev/selenium-webdriver-java/"
        self.driver.get(url + "slow-calculator.html")

    @allure.step("Установить задержку {value} секунд")
    def set_delay(self, value: str) -> None:
        """Устанавливает задержку вычисления.

        Args:
            value: значение задержки в секундах
        """
        delay = self.driver.find_element(By.CSS_SELECTOR, "#delay")
        delay.clear()
        delay.send_keys(value)

    @allure.step("Нажать кнопку {text}")
    def click_button(self, text: str) -> None:
        """Нажимает кнопку калькулятора.

        Args:
            text: текст кнопки
        """
        self.driver.find_element(
            By.XPATH, f"//span[text()='{text}']"
        ).click()

    @allure.step("Получить результат вычисления")
    def get_result(self) -> str:
        """Ожидает и возвращает результат вычисления.

        Returns:
            Строка с результатом вычисления
        """
        self.wait.until(
            EC.text_to_be_present_in_element(
                (By.CSS_SELECTOR, ".screen"), "15"
            )
        )
        return self.driver.find_element(By.CSS_SELECTOR, ".screen").text
