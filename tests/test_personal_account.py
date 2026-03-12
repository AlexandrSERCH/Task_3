import allure

from conftest import account_profile_page


@allure.epic("Личный кабинет")
@allure.feature("Переключение между вкладками")
class TestPersonalAccount:

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.tag("UI", "regress", "ЛК")
    @allure.title("Проверить переход на страницу 'Профиль'")
    def test_redirect_to_personal_account(self, user_is_auth, main_page, account_profile_page):
        main_page.click_account_button_in_header()

        actual_login = account_profile_page.get_value_from_login_field()
        actual_name = account_profile_page.get_text_from_name_field()
        expected_login, expected_name = user_is_auth

        assert expected_login == actual_login
        assert expected_name == actual_name

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.tag("UI", "regress", "ЛК")
    @allure.title("Проверить переход на страницу 'История заказов'")
    def test_redirect_to_order_history(self, user_is_auth, main_page, account_profile_page):
        main_page.click_account_button_in_header()
        account_profile_page.click_order_history()

        actual_url = account_profile_page.get_current_url()

        assert "account/order-history" in actual_url

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.tag("UI", "regress", "ЛК")
    @allure.title("Проверить выход из аккауета")
    def test_logout(self, user_is_auth, main_page, account_profile_page, login_page):
        main_page.click_account_button_in_header()
        account_profile_page.click_logout()

        login_page.success_visible_forgot_password_text_link()
