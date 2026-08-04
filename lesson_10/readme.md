  Allure отчёты:

 ## Описание
Автотесты для калькулятора и интернет-магазина на основе паттерна Page Object с подключением Allure для формирования отчётов.

## Структура
- `calculator_page.py` — страница калькулятора
- `login_page.py` — страница авторизации
- `main_page.py` — главная страница магазина
- `cart_page.py` — страница корзины
- `checkout_page.py` — страница оформления заказа
- `test_01_calc.py` — тест калькулятора
- `test_02_shop.py` — тест магазина

## Установка

pip install selenium allure-pytest

## Запуск тестов

pytest test_01_calc.py test_02_shop.py -v --alluredir=allure-results

## Просмотр отчёта

allure serve allure-results

Если allure не в PATH:

~\scoop\apps\allure\current\bin\allure.bat serve allure-results

Отчёт откроется в браузере автоматически.
