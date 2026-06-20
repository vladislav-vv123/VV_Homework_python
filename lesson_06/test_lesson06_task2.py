from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def test_session_storage_auth():
    driver = webdriver.Chrome()

    # Открываем сайт чтобы установить cookie для домена
    driver.get("https://gitflic.ru/")

    # Устанавливаем cookie первого пользователя
    driver.add_cookie({
        "name": "SESSION",
        "value": "ODRkNWI5YWQtZDNmOS00MjJjLWFlNWEtNWM3Yjk2MDkyZmFh"
    })

    # Обновляем и переходим на профиль
    driver.refresh()
    driver.get("https://gitflic.ru/user")

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "body"))
    )
    url_user1 = driver.current_url

    # Очищаем cookie
    driver.delete_all_cookies()

    # Cookie второго пользователя
    driver.get("https://gitflic.ru/")
    driver.add_cookie({
        "name": "SESSION",
        "value": "MzE3NWMyMTgtOTAxNS00ZWE2LWE3YTYtMTA2MDI1NWQ4OWFj"
    })

    driver.refresh()
    driver.get("https://gitflic.ru/user")

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "body"))
    )
    url_user2 = driver.current_url

    # Проверяем что URL различаются
    assert url_user1 != url_user2

    driver.quit()
