from selenium.webdriver.common.by import By


class HomePageLocators:

    # Раздел FAQ
    #  вопрос
    SPOILER_FAQ_1 = (By.ID, 'accordion__heading-0')
    # Первый ответ
    ANSWER_FAQ_1 = (By.CSS_SELECTOR, 'div[aria-labelledby="accordion__heading-0"]:not([hidden]) p')
    # Второй вопрос
    SPOILER_FAQ_2 = (By.ID, 'accordion__heading-1')
    # Второй ответ
    ANSWER_FAQ_2 = (By.CSS_SELECTOR, 'div[aria-labelledby="accordion__heading-1"]:not([hidden]) p')
    # Третий вопрос
    SPOILER_FAQ_3 = (By.ID, 'accordion__heading-2')
    # Третий ответ
    ANSWER_FAQ_3 = (By.CSS_SELECTOR, 'div[aria-labelledby="accordion__heading-2"]:not([hidden]) p')
    # Четвертый вопрос
    SPOILER_FAQ_4 = (By.ID, 'accordion__heading-3')
    # Четвертый ответ
    ANSWER_FAQ_4 = (By.CSS_SELECTOR, 'div[aria-labelledby="accordion__heading-3"]:not([hidden]) p')
    # Пятый вопрос
    SPOILER_FAQ_5 = (By.ID, 'accordion__heading-4')
    # Пятый ответ
    ANSWER_FAQ_5 = (By.CSS_SELECTOR, 'div[aria-labelledby="accordion__heading-4"]:not([hidden]) p')
    # Шестой вопрос
    SPOILER_FAQ_6 = (By.ID, 'accordion__heading-5')
    # Шестой ответ
    ANSWER_FAQ_6 = (By.CSS_SELECTOR, 'div[aria-labelledby="accordion__heading-5"]:not([hidden]) p')
    # Седьмой вопрос
    SPOILER_FAQ_7 = (By.ID, 'accordion__heading-6')
    # Седьмой ответ
    ANSWER_FAQ_7 = (By.CSS_SELECTOR, 'div[aria-labelledby="accordion__heading-6"]:not([hidden]) p')
    # Восьмой вопрос
    SPOILER_FAQ_8 = (By.ID, 'accordion__heading-7')
    # Восьмой ответ
    ANSWER_FAQ_8 = (By.CSS_SELECTOR, 'div[aria-labelledby="accordion__heading-7"]:not([hidden]) p')
    # Последний вопрос
    SPOILER_FAQ_LAST = (By.XPATH, '//*[contains(@class,"accordion__item")][last()]')

    #Кнопки Заказать
    #Кнопка Заказать в шапке страницы
    BUTTON_ORDER_HEADER = (By.CLASS_NAME, 'Button_Button__ra12g')
    #Кнопка Заказать в теле страницы
    BUTTON_ORDER_BODY = (By.XPATH, '//*[contains(@class, "Home_FinishButton__1_cWm")]/button')

    #Лого Самокат
    LOGO_SCOOTER= (By.XPATH, '//*[contains(@class,"Header_LogoScooter")]')
    #Лого Яндекс
    LOGO_YANDEX= (By.XPATH, '//*[contains(@class,"Header_LogoYandex")]')
