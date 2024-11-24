import allure

from locators.home_page_locators import HomePageLocators
from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage


class OrderPage(BasePage):

    @allure.step('Заполнить поле Имя')
    def send_name(self, name):
        self.scroll_to_element(OrderPageLocators.INPUT_ORDER_NAME)
        self.find_clickable_element(OrderPageLocators.INPUT_ORDER_NAME).send_keys(name)

    @allure.step('Заполнить поле Фамилия')
    def send_surname(self, surname):
        self.scroll_to_element(OrderPageLocators.INPUT_ORDER_SURNAME)
        self.find_clickable_element(OrderPageLocators.INPUT_ORDER_SURNAME).send_keys(surname)

    @allure.step('Заполнить поле Адрес')
    def send_address(self, address):
        self.scroll_to_element(OrderPageLocators.INPUT_ORDER_ADDRESS)
        self.find_clickable_element(OrderPageLocators.INPUT_ORDER_ADDRESS).send_keys(address)

    @allure.step('Заполнить поле Станция метро')
    def send_metro(self, metro):
        self.scroll_to_element(OrderPageLocators.INPUT_ORDER_METRO)
        input_metro = self.find_clickable_element(OrderPageLocators.INPUT_ORDER_METRO)
        input_metro.click()
        input_metro.send_keys(metro)
        self.find_clickable_element(OrderPageLocators.FIRST_METRO).click()

    @allure.step('Заполнить поле Телефон')
    def send_phone(self, phone):
        self.scroll_to_element(OrderPageLocators.INPUT_ORDER_PHONE)
        self.find_clickable_element(OrderPageLocators.INPUT_ORDER_PHONE).send_keys(phone)

    @allure.step('Нажать кнопку Далее')
    def click_button_next(self):
        self.scroll_to_element(OrderPageLocators.BUTTON_ORDER_NEXT)
        self.find_clickable_element(OrderPageLocators.BUTTON_ORDER_NEXT).click()

    @allure.step('Заполнение формы Для кого самокат')
    def submit_for_person(self, name, surname, address, metro, phone):
        self.send_name(name)
        self.send_surname(surname)
        self.send_address(address)
        self.send_metro(metro)
        self.send_phone(phone)
        self.click_button_next()

    @allure.step('Выбрать текущую дату поля Когда привезти самокат')
    def send_today_rent(self):
        self.scroll_to_element(OrderPageLocators.INPUT_ORDER_WHEN_DATE)
        self.find_clickable_element(OrderPageLocators.INPUT_ORDER_WHEN_DATE).click()
        self.find_clickable_element(OrderPageLocators.TODAY_DATE_CALENDAR).click()

    @allure.step('Выбрать Срок аренды')
    def select_period(self, locator_period_days):
        self.scroll_to_element(OrderPageLocators.INPUT_ORDER_PERIOD)
        self.find_clickable_element(OrderPageLocators.INPUT_ORDER_PERIOD).click()
        self.find_clickable_element(locator_period_days).click()

    @allure.step('Выбрать Цвет самоката')
    def select_color(self, locator_color):
        self.scroll_to_element(locator_color)
        self.find_clickable_element(locator_color).click()

    @allure.step('Заполнить Комментарий для курьера')
    def send_comment(self):
        self.scroll_to_element(OrderPageLocators.INPUT_ORDER_COMMENT)
        self.find_clickable_element(OrderPageLocators.INPUT_ORDER_COMMENT).send_keys("Комментарий для курьера")


    @allure.step('Нажать кнопку Завершить')
    def click_button_finish(self):
        self.scroll_to_element(OrderPageLocators.BUTTON_ORDER_FINISH)
        self.find_clickable_element(OrderPageLocators.BUTTON_ORDER_FINISH).click()

    @allure.step('Заполнить Комментарий для курьера')
    def click_yes(self):
        self.scroll_to_element(OrderPageLocators.BUTTON_ORDER_YES)
        self.find_clickable_element(OrderPageLocators.BUTTON_ORDER_YES).click()

    @allure.step('Проверить что Заказ оформлен')
    def check_successfully_order(self):
        return self.find_clickable_element(OrderPageLocators.ORDER_SUCCESSFULLY_CREATE).is_displayed()

    @allure.step('Заполнение формы Для кого самокат')
    def submit_for_rent(self):
        self.send_today_rent()
        self.select_period(OrderPageLocators.LIST_PERIOD_THREE)
        self.select_color(OrderPageLocators.COLOR_BLACK_PEARL)
        self.send_comment()
        self.click_button_finish()
        self.click_yes()