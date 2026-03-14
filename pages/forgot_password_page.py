import allure

from constants import forgot_password_url
from locators.forgot_password_page_locators import FORGOT_PASSWORD_TITLE, EMAIL_INPUT, RECOVERY_BUTTON
from pages.base_page import BasePage


class ForgotPasswordPage(BasePage):

    @allure.step("Открыть страницу восстановления пароля")
    def open(self):
        self._open_page(forgot_password_url())

    @allure.step("Получить заголовок страницы восстановления пароля")
    def get_title_text(self):
        return self._get_text(FORGOT_PASSWORD_TITLE)

    @allure.step("Ввести email")
    def send_email(self, email: str):
        self._send_keys(EMAIL_INPUT, email)

    @allure.step("Нажать кнопку 'Восстановить'")
    def click_recovery_button(self):
        self._click(RECOVERY_BUTTON)
