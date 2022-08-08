import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--browser_name',      # возможность выбрать браузер
                     action='store',
                     default="chrome",      # по умолчанию "chrome"
                     help="Choose browser: chrome or firefox")

    parser.addoption('--language',          # возможность выбрать язык
                     action='store',
                     default='fr',          # не выбран по умолчанию
                     help="Choose user languages: en/ru/es/fr.......(etc)")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    user_language = request.config.getoption("language")
    browser = None
    if browser_name == "chrome":                    # если для теста выбран браузер "chrome"
        print("\nstart chrome browser for test..")
        options = Options()                         # выбираем язык тестового окружения
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":                 # если для теста выбран браузер "firefox"
        print("\nstart firefox browser for test..")
        fp = webdriver.FirefoxProfile()             # выбираем язык тестового окружения
        fp.set_preference("intl.accept_languages", user_language)
        browser = webdriver.Firefox(firefox_profile=fp)
    else:
        raise pytest.UsageError(f'--browser_name should be chrome or firefox\nБраузер должен быть chrome или firefox')
    yield browser
    print("\nquit browser..")
    browser.quit()