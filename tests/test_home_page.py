import allure
import pytest

from locators.base_page_locators import BasePageLocators
from locators.home_page_locators import HomePageLocators
from pages.home_page import HomePage
from tests_data import tested_faqs, BASE_URL, DZEN_URL


class TestFAQSection:

    @allure.title('Проверить: если нажать на логотип «Самоката», попадёшь на главную страницу «Самоката».')
    def test_click_logo_scooter_open_home_page(self, driver):
        home_page = HomePage(driver)
        home_page.click_button_order_header()
        home_page.click_logo_scooter()
        assert home_page.get_current_url() == BASE_URL

    @allure.title('Проверить: если нажать на логотип Яндекса, в новом окне через редирект откроется главная страница Дзена.')
    def test_click_logo_scooter_open_dzen_page(self, driver):
        home_page = HomePage(driver)
        home_page.click_logo_yandex()
        home_page.switch_to_new_tab()
        home_page.wait_load_dzen()
        assert DZEN_URL in home_page.get_current_url()

    @allure.title('Проверить: Выпадающий список в разделе «Вопросы о важном»')
    @pytest.mark.parametrize('question_locator, answer_locator, tested_text', [
        (HomePageLocators.SPOILER_FAQ_1, HomePageLocators.ANSWER_FAQ_1, tested_faqs[0]["answer"]),
        (HomePageLocators.SPOILER_FAQ_2, HomePageLocators.ANSWER_FAQ_2, tested_faqs[1]["answer"]),
        (HomePageLocators.SPOILER_FAQ_3, HomePageLocators.ANSWER_FAQ_3, tested_faqs[2]["answer"]),
        (HomePageLocators.SPOILER_FAQ_4, HomePageLocators.ANSWER_FAQ_4, tested_faqs[3]["answer"]),
        (HomePageLocators.SPOILER_FAQ_5, HomePageLocators.ANSWER_FAQ_5, tested_faqs[4]["answer"]),
        (HomePageLocators.SPOILER_FAQ_6, HomePageLocators.ANSWER_FAQ_6, tested_faqs[5]["answer"]),
        (HomePageLocators.SPOILER_FAQ_7, HomePageLocators.ANSWER_FAQ_7, tested_faqs[6]["answer"]),
        (HomePageLocators.SPOILER_FAQ_8, HomePageLocators.ANSWER_FAQ_8, tested_faqs[7]["answer"])
    ])
    def test_click_question_shows_answer(self, driver, question_locator, answer_locator, tested_text):
        home_page = HomePage(driver)
        home_page.click_question(question_locator)
        answer_text = home_page.get_answer_text(answer_locator)
        assert answer_text == tested_text