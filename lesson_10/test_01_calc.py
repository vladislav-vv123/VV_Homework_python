import allure
from selenium import webdriver
from calculator_page import CalculatorPage


@allure.title("Проверка калькулятора с задержкой 45 секунд")
@allure.description("Тест проверяет что 7 + 8 = 15 с задержкой 45 секунд")
@allure.feature("Калькулятор")
@allure.severity(allure.severity_level.NORMAL)
def test_calc():
    driver = webdriver.Chrome()

    page = CalculatorPage(driver)

    with allure.step("Открыть страницу калькулятора"):
        page.open()

    with allure.step("Установить задержку 45 секунд"):
        page.set_delay("45")

    with allure.step("Нажать кнопки 7 + 8 ="):
        page.click_button("7")
        page.click_button("+")
        page.click_button("8")
        page.click_button("=")

    with allure.step("Получить результат"):
        result = page.get_result()

    driver.quit()

    with allure.step("Проверить что результат равен 15"):
        assert result == "15"
