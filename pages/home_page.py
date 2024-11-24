import allure

from locators.home_page_locators import HomePageLocators
from pages.base_page import BasePage


class HomePage(BasePage):

    @allure.step('Нажать на вопрос')
    def click_question(self, question_locator):
        self.scroll_to_element(HomePageLocators.SPOILER_FAQ_LAST)
        self.find_clickable_element(question_locator).click()

    @allure.step('Получить текста ответа')
    def get_answer_text(self, answer_locator):
        answer_text = self.driver.find_element(*answer_locator).text
        return answer_text

    @allure.step('Нажать кнопку Заказать в шапке страницы')
    def click_button_order_header(self):
        self.scroll_to_element(HomePageLocators.BUTTON_ORDER_HEADER)
        self.find_clickable_element(HomePageLocators.BUTTON_ORDER_HEADER).click()

    @allure.step('Нажать кнопку Заказать в теле страницы')
    def click_button_order_body(self):
        self.scroll_to_element(HomePageLocators.BUTTON_ORDER_BODY)
        self.find_clickable_element(HomePageLocators.BUTTON_ORDER_BODY).click()

    @allure.step('Нажать кнопку Лого Самокат')
    def click_logo_scooter(self):
        self.scroll_to_element(HomePageLocators.LOGO_SCOOTER)
        self.find_clickable_element(HomePageLocators.LOGO_SCOOTER).click()

    @allure.step('Нажать кнопку Лого Яндекс')
    def click_logo_yandex(self):
        self.scroll_to_element(HomePageLocators.LOGO_YANDEX)
        self.find_clickable_element(HomePageLocators.LOGO_YANDEX).click()