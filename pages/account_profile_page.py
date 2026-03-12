import allure

from locators.account_profile_page_locators import NAME_FIELD, LOGIN_FIELD, ORDER_HISTORY_LINK, LOGOUT_BUTTON
from pages.base_page import BasePage


class AccountProfilePage(BasePage):

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

    @allure.step("Получить текущую ссылку")
    def get_current_url(self):
        return self._get_current_url()