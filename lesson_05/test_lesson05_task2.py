from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_form_submission():
    driver = webdriver.Chrome()
    driver.get("https://httpbin.org/forms/post")

    name_field = driver.find_element(By.NAME, "custname")
    name_field.send_keys("Vladislav")

    submit = driver.find_element(By.XPATH, "//button[text()='Submit order']")
    submit.click()

    WebDriverWait(driver, 10).until(
        EC.url_changes("https://httpbin.org/forms/post")
    )

    assert driver.current_url != "https://httpbin.org/forms/post"

    driver.quit()
