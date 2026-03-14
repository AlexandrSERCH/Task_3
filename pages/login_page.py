import allure

from constants import login_page_url
from locators.login_page_locators import FORGOT_PASSWORD_TEXT_LINK, EMAIL_FIELD, PASSWORD_FIELD, LOGIN_BUTTON
from pages.base_page import BasePage


class LoginPage(BasePage):

    @allure.step("Открыть страницу авторизации")
    def open(self):
        self._open_page(login_page_url())

    @allure.step("Успешное отображение элемента 'Восстановить пароль'")
    def success_visible_forgot_password_text_link(self):
        assert self._is_visible(FORGOT_PASSWORD_TEXT_LINK)

    @allure.step("Нажать на гиперссылку 'Восстановить пароль'")
    def click_recovey_password_text_link(self):
        self._click(FORGOT_PASSWORD_TEXT_LINK)

    @allure.step("Авторизоваться")
    def auth(self, email: str, password: str):
        self._send_keys(EMAIL_FIELD, email)
        self._send_keys(PASSWORD_FIELD, password)
        self._click(LOGIN_BUTTON)
        self._wait_for_url_not_contains("login")