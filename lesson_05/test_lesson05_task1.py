from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_navigation():
    driver = webdriver.Chrome()
    driver.get("https://httpbin.org/")

    start_url = driver.current_url

    link = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "HTML form"))
    )
    link.click()

    assert "/forms/post" in driver.current_url

    driver.back()

    assert driver.current_url == start_url

    driver.quit()
