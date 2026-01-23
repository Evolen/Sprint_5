from selenium.webdriver.common.by import By


class Locators:
    

    PERSONAL_ACCOUNT = (By.XPATH,  ".//*[text() = 'Личный Кабинет']") #Кнопка Личный кабинет
    REG_BUTTON = (By.XPATH, ".//*[text() = 'Зарегистрироваться']") #Кнопка регистрации из формы Вход
    NAME = (By.NAME, "name") #Заполнение полей "Имя" и "Email" при регистрации
    PASSWORD = (By.NAME, "Пароль") #Заполнение поля "Пароль" при регистрации
    REG_BUTTON_FINALE = (By.XPATH, ".//*[text() = 'Зарегистрироваться']") #Кнопка подтверждения регистрации
    PASSWORD_ERROR = (By.XPATH, ".//*[@class = 'input__error text_type_main-default']") #Ошибка "Некорректный пароль"
    LOGIN_BUTTON = (By.XPATH,".//*[@class = 'button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg']" ) #Кнопка входа с главной страницы
    EMAIL = (By.XPATH, ".//*[@class = 'text input__textfield text_type_main-default']") #Поле ввода Email для входа
    PASSWORD_LOGIN = (By.NAME, "Пароль") #Поле ввода пароля для входа
    LOGIN_BUTTON_FINALLY = (By.XPATH, ".//*[text() = 'Войти']") #Подтверждение входа в аккаунт
    BUTTON_ORDER = (By.XPATH, ".//*[text() = 'Оформить заказ']") #Кнопка "Оформить заказ" на главной странице после входа
    RECOVERY_PASS = (By.XPATH, ".//*[text() = 'Восстановить пароль']") #Кнопка "Восстановить пароль" от акаунта 
    RECOVERY_PASS_LOGIN = (By.XPATH, ".//*[text() = 'Войти']") #Кнопка Войти в аккаунт на сранице смены пароля 
    CONSTRUCTOR = (By.XPATH, ".//*[text() = 'Конструктор']") #Переход на страницу Конструктор
    CONSTRUCTOR_CHECK = (By.XPATH, ".//*[@class = 'text text_type_main-large mb-5 mt-10']") #Проверка перехода на вкладку "Конструктор" из личного кабинета
    LOGO = (By.XPATH, ".//*[@class = 'AppHeader_header__logo__2D0X2']") #Переход на страницу "Конструктор" через лого Stellar Burgers
    EXIT_BUTTON = (By.XPATH, ".//*[text() = 'Выход']") #Кнопка выхода из аккаунта
    BUN = (By.XPATH, ".//span[text() = 'Булки']") #Переход в раздел Булки
    SAUCES = (By.XPATH, ".//span[text() = 'Соусы']") #Переход в раздел Соусы
    FILLINGS = (By.XPATH, ".//span[text() = 'Начинки']") #Переход в раздел Начинки
    CHECK_FORM_ENTRANCE = (By.XPATH, ".//*[text() = 'Вход']")#Проверка формы входа
    SAUCES_CHOICE = (By.XPATH, ".//h2[text() = 'Соусы']")
    BUN_CHOICE = (By.XPATH, ".//h2[text() = 'Булки']") 
    FILLINGS_CHOICE = (By.XPATH, ".//h2[text() = 'Начинки']")
    
    
    