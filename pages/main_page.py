from pages.base_page import BasePage            # Импорт базового класса BasePage


class MainPage(BasePage):    # Создание класса MainPage, наследующего класс BasePage
    def __init__(self, *args, **kwargs): # Заглушка
        super(MainPage, self).__init__(*args, **kwargs)

