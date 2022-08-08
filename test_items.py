# pytest -s -v --language=fr test_items.py
# pytest -s -v --language=en test_items.py
# pytest --language=en test_items.py


import time
from selenium.webdriver.common.by import By


url = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'


def test_contains_button_add_is_basket(browser):

    browser.get(url)
    browser.implicitly_wait(5)
    # time.sleep(30)
    assert browser.find_elements(By.CSS_SELECTOR, '#add_to_basket_form button'), "\033[1m\033[31m КНОПКИ НЕТ "



