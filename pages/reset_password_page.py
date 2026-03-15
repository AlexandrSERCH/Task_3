import allure

from locators.reset_password_page_locators import PASSWORD_FIELD, TOGGLE_PASSWORD_VISIBILITY_BUTTON
from pages.base_page import BasePage


class ResetPasswordPage(BasePage):

    @allure.step("Успешное отображение поля 'Пароль'")
    def success_visible_password_field(self):
        assert self._is_visible(PASSWORD_FIELD)

    @allure.step("Заполнить поле 'Пароль'")
    def send_password(self, text: str):
        self._send_keys(PASSWORD_FIELD, text)

    @allure.step("Нажать на иконку показать/скрыть пароль")
    def click_toggle_password_visibility_button(self):
        self._click(TOGGLE_PASSWORD_VISIBILITY_BUTTON)

    @allure.step("Получить значение атрибута 'type' поля 'Пароль'")
    def get_value_attribute_type_field_password(self):
        return self._get_attribute_value(PASSWORD_FIELD, "type")

    @allure.step("Проверить, что значение в поле 'Пароль' скрыто")
    def value_in_field_password_is_hidden(self):
        result = self.get_value_attribute_type_field_password()
        assert "password" == result, f"Вместо типа 'password' содержится значение: '{result}'"

    @allure.step("Проверить, что значение в поле 'Пароль' отображается текстом")
    def value_in_field_password_is_visible(self):
        result = self.get_value_attribute_type_field_password()
        assert "text" == result, f"Вместо типа 'text' содержится значение: '{result}'"