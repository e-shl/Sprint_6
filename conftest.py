import pytest
from selenium import webdriver

from tests_data import BASE_URL


@pytest.fixture
def driver():
    options = webdriver.FirefoxOptions()
    options.add_argument("--window-size=1920,1080")
    options.add_argument('--headless')
    driver = webdriver.Firefox(options=options)
    driver.get(BASE_URL)
    yield driver
    driver.quit()