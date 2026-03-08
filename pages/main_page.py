import allure

from constants import site_url
from locators.header_locators import PERSONAL_ACCOUNT_BUTTON
from pages.base_page import BasePage


class MainPage(BasePage):

    @allure.step("Открыть главную страницу")
    def open(self):
        self._open_page(site_url())

    @allure.step("Нажать на кнопку 'Личный кабинет' в хедере")
    def click_account_button_in_header(self):
        self._click(PERSONAL_ACCOUNT_BUTTON)