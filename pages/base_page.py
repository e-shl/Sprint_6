import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators.base_page_locators import BasePageLocators


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Получить кликабельный элемент')
    def find_clickable_element(self, locator):
        WebDriverWait(self.driver, 200).until(expected_conditions.element_to_be_clickable(locator))
        return self.driver.find_element(*locator)

    @allure.step('Прокрутить к элементу')
    def scroll_to_element(self, locator):
        self.driver.execute_script('arguments[0].scrollIntoView();', self.driver.find_element(*locator))

    @allure.step('Принять Куки')
    def click_button_cookie(self):
        self.scroll_to_element(BasePageLocators.BUTTON_COOKIE_CONFIRM)
        self.find_clickable_element(BasePageLocators.BUTTON_COOKIE_CONFIRM).click()

    @allure.step('Перейти на другую вкладку')
    def switch_to_new_tab(self):
        self.driver.switch_to.window(self.driver.window_handles[1])

    @allure.step('Получить URL текущей страницы')
    def get_current_url(self):
        return self.driver.current_url

    @allure.step('Дождаться загрузки DZEN')
    def wait_load_dzen(self):
        self.find_clickable_element(BasePageLocators.YANDEX_SEARCH)
