from selenium.webdriver.common.by import By


class BasePageLocators:

    # Кнопка "да все привыкли" - закрыть окно Куки
    BUTTON_COOKIE_CONFIRM = (By.ID, 'rcc-confirm-button')

    # Лого Поиск Яндекс в DZEN
    YANDEX_SEARCH = (By.XPATH, '//*[contains(text(),"Поиск Яндекс")]')


