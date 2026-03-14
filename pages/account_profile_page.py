import allure

from constants import account_profile_url
from locators.account_profile_page_locators import NAME_FIELD, LOGIN_FIELD, ORDER_HISTORY_LINK, LOGOUT_BUTTON, \
    FIRST_ORDER_NUMBER
from pages.base_page import BasePage


class AccountProfilePage(BasePage):

    @allure.step("Открыть страницу 'Личный кабинет'")
    def open(self):
        self._open_page(account_profile_url())

    @allure.step("Получить текст из поля 'Имя'")
    def get_text_from_name_field(self):
        return self._get_value(NAME_FIELD)

    @allure.step("Получить текст из поля 'Логин'")
    def get_value_from_login_field(self):
        return self._get_value(LOGIN_FIELD)

    @allure.step("Нажать в сайд-баре на кнокпу 'История заказов'")
    def click_order_history(self):
        self._click(ORDER_HISTORY_LINK)

    @allure.step("Нажать в сайд-баре на кнокпу 'Выход'")
    def click_logout(self):
        self._click(LOGOUT_BUTTON)

    @allure.step("Получить номер первого заказа из истории заказов")
    def get_first_order_number(self) -> str:
        return self._get_text(FIRST_ORDER_NUMBER)

    @allure.step("Получить текущую ссылку")
    def get_current_url(self):
        return self._get_current_url()
