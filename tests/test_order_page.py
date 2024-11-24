import allure
import pytest

from pages.home_page import HomePage
from pages.order_page import OrderPage
from tests_data import user_2, user_1


class TestOrderForm:

    @allure.title('Проверить: Успешное создание заказа через кнопку Заказать в шапке страницы')
    @pytest.mark.parametrize('name, surname, address, metro, phone', [user_1])
    def test_creating_order_from_button_header(self, driver, name, surname, address, metro, phone):
        home_page = HomePage(driver)
        home_page.click_button_order_header()
        order_page = OrderPage(driver)
        order_page.submit_for_person(name, surname, address, metro, phone)
        order_page.submit_for_rent()
        assert order_page.check_successfully_order()

    @allure.title('Проверить: Успешное создание заказа через кнопку Заказать в теле страницы')
    @pytest.mark.parametrize('name, surname, address, metro, phone', [user_2])
    def test_creating_order_from_button_body(self, driver, name, surname, address, metro, phone):
        home_page = HomePage(driver)
        home_page.click_button_cookie()
        home_page.click_button_order_body()
        order_page = OrderPage(driver)
        order_page.submit_for_person(name, surname, address, metro, phone)
        order_page.submit_for_rent()
        assert order_page.check_successfully_order()