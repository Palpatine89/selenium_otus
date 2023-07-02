import pytest
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions


def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome")
    parser.addoption("--maximize", action="store_true")
    parser.addoption("--headless", action="store_true")
    parser.addoption("--url", action="store", default="http://10.0.2.15:8081")


@pytest.fixture()
def browser(request):
    browser_name = request.config.getoption("--browser")
    maximize = request.config.getoption("--maximize")
    headless = request.config.getoption("--headless")
    url = request.config.getoption("--url")

    if browser_name == "firefox":
        options = FirefoxOptions()
        if headless:
            options.headless = True
        driver = webdriver.Firefox(options=options)

    elif browser_name == "chrome":
        service = Service()
        options = ChromeOptions()
        if headless:
            options.add_argument("headless=new")
        driver = webdriver.Chrome(service=service, options=options)

    elif browser_name == "edge":
        options = EdgeOptions()
        if headless:
            options.add_argument("headless=new")
        driver = webdriver.Edge(options=options)

    elif browser_name == "yandex":
        service = Service(executable_path=os.path.expanduser("~/drivers/yandexbrowserdriver/yandexdriver"))
        options = ChromeOptions()
        if headless:
            options.add_argument("headless=new")
        driver = webdriver.Chrome(options=options, service=service)

    else:
        raise ValueError(f"Driver {browser_name} not supported.")

    if maximize:
        driver.maximize_window()

    driver.get(url)
    driver.url = url

    yield driver

    driver.quit()
