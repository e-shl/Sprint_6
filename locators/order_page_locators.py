from selenium.webdriver.common.by import By


class OrderPageLocators:

    # Поле Имя
    INPUT_ORDER_NAME = (By.XPATH, '//input[contains(@placeholder,"Имя")]')
    # Поле Фамилия
    INPUT_ORDER_SURNAME = (By.XPATH, '//input[contains(@placeholder,"Фамилия")]')
    # Поле Адрес
    INPUT_ORDER_ADDRESS = (By.XPATH, '//input[contains(@placeholder,"Адрес")]')
    # Поле Станция метро
    INPUT_ORDER_METRO = (By.XPATH, '//input[contains(@placeholder,"Станция метро")]')
    FIRST_METRO = (By.XPATH, '//*[@class="select-search__select"]//li[1]')
    # Поле Телефон
    INPUT_ORDER_PHONE = (By.XPATH, '//input[contains(@placeholder,"Телефон")]')
    # Кнопка Далее
    BUTTON_ORDER_NEXT = (By.XPATH, '//*[contains(@class, "Order_NextButton")]/button')
    # Поле Когда привезти самокат
    INPUT_ORDER_WHEN_DATE = (By.XPATH, '//input[contains(@placeholder,"Когда привезти самокат")]')
    # Сегодняшняя дата в календаре
    TODAY_DATE_CALENDAR = (By.CLASS_NAME, 'react-datepicker__day--today')
    # Поле Срок аренды
    INPUT_ORDER_PERIOD = (By.XPATH, '//*[contains(text(),"Срок аренды")]')
    # Двое суток в открытом списке сроков аренды
    LIST_PERIOD_THREE = (By.XPATH, '//*[@class = "Dropdown-menu"]/div[text() ="двое суток"]')
    # Цвет самоката чёрный жемчуг
    COLOR_BLACK_PEARL = (By.XPATH, '//*[text()="Цвет самоката"]/../*[text()="чёрный жемчуг"]')
    # Поле Комментарий для курьера
    INPUT_ORDER_COMMENT = (By.XPATH, '//input[contains(@placeholder,"Комментарий для курьера")]')
    # Кнопка Заказать
    BUTTON_ORDER_FINISH = (By.XPATH, '//*[contains(@class, "Order_Buttons")]/button[text()="Заказать"]')
    # Кнопка Да
    BUTTON_ORDER_YES = (By.XPATH, '//button[text()="Да"]')
    # Окно Заказ оформлен
    ORDER_SUCCESSFULLY_CREATE = (By.XPATH, '//*[text()="Заказ оформлен"]')