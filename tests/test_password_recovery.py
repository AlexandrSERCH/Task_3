import allure
import pytest


@pytest.fixture
def open_reset_password_page(forgot_password_page, reset_password_page):
    forgot_password_page.open()
    forgot_password_page.send_email("email@email.ru")
    forgot_password_page.click_recovery_button()
    return reset_password_page


@allure.epic("Личный кабинет")
@allure.feature("Восстановление пароля")
class TestPasswordRecovery:

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.tag("UI", "regress", "ЛК")
    @allure.title("Проверить отображение гиперссылки 'Восстановить пароль'")
    def test_redirect_to_login_page_by_login_button(self, main_page, login_page):
        main_page.open()
        main_page.click_account_button_in_header()
        login_page.success_visible_forgot_password_text_link()

    @allure.severity(allure.severity_level.NORMAL)
    @allure.tag("UI", "regress", "ЛК")
    @allure.title("Переход на страницу восстановления пароля по гиперссылке 'Восстановить пароль'")
    def test_redirect_to_forgot_password_page_by_text_link(self, main_page, login_page, forgot_password_page):
        login_page.open()
        login_page.click_recovey_password_text_link()
        actual_title = forgot_password_page.get_title_text()
        expected_title = "Восстановление пароля"

        with allure.step(f"Проверить, что ФР: '{actual_title}' соответствует ОР: '{expected_title}'"):
            assert expected_title == actual_title

    @allure.severity(allure.severity_level.NORMAL)
    @allure.tag("UI", "regress", "ЛК")
    @allure.title("Ввод почты на странице восстановления пароля и переход к указанию нового пароля")
    def test_send_email_and_redirect_to_send_new_password(self, forgot_password_page, reset_password_page):
        forgot_password_page.open()
        forgot_password_page.send_email("email@email.ru")
        forgot_password_page.click_recovery_button()

        reset_password_page.success_visible_password_field()

    @allure.severity(allure.severity_level.MINOR)
    @allure.tag("UI", "regress", "ЛК")
    @allure.title("Отображение/скрытие пароля при нажатии на иконку 'глаз'")
    def test_toggle_password_visibility_by_eye_icon(self, open_reset_password_page, reset_password_page):
        reset_password_page.send_password("123456qA")

        reset_password_page.click_toogle_password_visability_button()

        with allure.step("Успешное отображение пароля"):
            reset_password_page.value_in_field_password_is_visible()

        reset_password_page.click_toogle_password_visability_button()

        with allure.step("Успешная маскировка пароля"):
            reset_password_page.value_in_field_password_is_hidden()
