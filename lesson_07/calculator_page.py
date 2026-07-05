from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 60)

    def open(self):
        url = "https://bonigarcia.dev/selenium-webdriver-java/"
        self.driver.get(url + "slow-calculator.html")

    def set_delay(self, value):
        delay = self.driver.find_element(By.CSS_SELECTOR, "#delay")
        delay.clear()
        delay.send_keys(value)

    def click_button(self, text):
        self.driver.find_element(
            By.XPATH, f"//span[text()='{text}']"
        ).click()

    def get_result(self):
        self.wait.until(
            EC.text_to_be_present_in_element(
                (By.CSS_SELECTOR, ".screen"), "15"
            )
        )
        return self.driver.find_element(By.CSS_SELECTOR, ".screen").text
