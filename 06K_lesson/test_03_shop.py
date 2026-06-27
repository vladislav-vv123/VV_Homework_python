from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_shop():
    driver = webdriver.Firefox()
    driver.get("https://www.saucedemo.com/")

    # Авторизация
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    # Ждём загрузки каталога
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "inventory_list"))
    )

    # Добавляем товары в корзину
    driver.find_element(
        By.XPATH, "//button[@data-test='add-to-cart-sauce-labs-backpack']"
    ).click()
    driver.find_element(
        By.XPATH, "//button[@data-test='add-to-cart-sauce-labs-bolt-t-shirt']"
    ).click()
    driver.find_element(
        By.XPATH, "//button[@data-test='add-to-cart-sauce-labs-onesie']"
    ).click()

    # Переходим в корзину
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    # Нажимаем Checkout
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "checkout"))
    )
    driver.find_element(By.ID, "checkout").click()

    # Заполняем форму
    driver.find_element(By.ID, "first-name").send_keys("Владислав")
    driver.find_element(By.ID, "last-name").send_keys("Веденеев")
    driver.find_element(By.ID, "postal-code").send_keys("630001")
    driver.find_element(By.ID, "continue").click()

    # Читаем итоговую стоимость
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "summary_total_label"))
    )
    total = driver.find_element(By.CLASS_NAME, "summary_total_label").text

    driver.quit()

    # Проверяем итоговую сумму
    assert total == "Total: $58.29"
