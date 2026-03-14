import allure

from constants import site_url
from locators.header_locators import PERSONAL_ACCOUNT_BUTTON, CONSTRUCTOR_BUTTON, ORDER_FEED_BUTTON
from locators.main_page_locators import (
    CONSTRUCTOR_TITLE, ORDER_FEED_TITLE,
    FIRST_INGREDIENT, FIRST_INGREDIENT_NAME,
    THIRD_INGREDIENT, THIRD_INGREDIENT_COUNTER, CONSTRUCTOR_DROP_ZONE,
    ORDER_BUTTON, ORDER_MODAL_NUMBER, ORDER_MODAL_TEXT, ORDER_MODAL_CLOSE_BUTTON,
    INGREDIENT_MODAL, INGREDIENT_MODAL_NAME, INGREDIENT_MODAL_CLOSE_BUTTON,
)
from pages.base_page import BasePage


class MainPage(BasePage):

    @allure.step("Открыть главную страницу")
    def open(self):
        self._open_page(site_url())

    @allure.step("Нажать на кнопку 'Личный кабинет' в хедере")
    def click_account_button_in_header(self):
        self._click(PERSONAL_ACCOUNT_BUTTON)

    @allure.step("Нажать на кнопку 'Конструктор' в хедере")
    def click_constructor_button_in_header(self):
        self._click(CONSTRUCTOR_BUTTON)

    @allure.step("Успешное отображение заголовка 'Соберите бургер'")
    def success_visible_constructor_title(self):
        assert self._is_visible(CONSTRUCTOR_TITLE)

    @allure.step("Нажать на кнопку 'Лента Заказов' в хедере")
    def click_order_feed_button_in_header(self):
        self._click(ORDER_FEED_BUTTON)

    @allure.step("Успешное отображение заголовка на странице 'Лента заказов'")
    def success_visible_order_feed_title(self):
        assert self._is_visible(ORDER_FEED_TITLE)

    @allure.step("Получить текущую ссылку")
    def get_current_url(self):
        return self._get_current_url()

    @allure.step("Получить название первого ингредиента в списке")
    def get_first_ingredient_name(self):
        return self._get_text(FIRST_INGREDIENT_NAME)

    @allure.step("Кликнуть на первый ингредиент в списке")
    def click_first_ingredient(self):
        self._click(FIRST_INGREDIENT)

    @allure.step("Успешное отображение модального окна 'Детали ингредиента'")
    def success_visible_ingredient_modal(self):
        assert self._is_visible(INGREDIENT_MODAL)

    @allure.step("Получить название ингредиента из модального окна")
    def get_ingredient_modal_name(self):
        return self._get_text(INGREDIENT_MODAL_NAME)

    @allure.step("Закрыть модальное окно кликом по крестику")
    def click_close_ingredient_modal(self):
        self._click_without_overlay_wait(INGREDIENT_MODAL_CLOSE_BUTTON)

    @allure.step("Проверить, что модальное окно закрылось")
    def success_invisible_ingredient_modal(self):
        assert self._is_invisible(INGREDIENT_MODAL)

    @allure.step("Получить значение счётчика третьего ингредиента")
    def get_third_ingredient_counter(self) -> int:
        return self._get_counter_value(THIRD_INGREDIENT_COUNTER)

    @allure.step("Перетащить первый ингредиент в конструктор")
    def drag_first_ingredient_to_constructor(self):
        self._drag_and_drop(FIRST_INGREDIENT, CONSTRUCTOR_DROP_ZONE)

    @allure.step("Перетащить третий ингредиент в конструктор")
    def drag_third_ingredient_to_constructor(self):
        self._drag_and_drop(THIRD_INGREDIENT, CONSTRUCTOR_DROP_ZONE)

    @allure.step("Нажать кнопку 'Оформить заказ'")
    def click_order_button(self):
        self._click(ORDER_BUTTON)

    @allure.step("Получить номер заказа из модального окна")
    def get_order_modal_number(self) -> str:
        self.wait.until(
            lambda d: d.find_element(*ORDER_MODAL_NUMBER).text not in ("9999", "")
        )
        return self._get_text(ORDER_MODAL_NUMBER)

    @allure.step("Получить текст подтверждения заказа из модального окна")
    def get_order_modal_text(self) -> str:
        return self._get_text(ORDER_MODAL_TEXT)

    @allure.step("Закрыть модальное окно подтверждения заказа")
    def close_order_confirmation_modal(self):
        self._click_js(ORDER_MODAL_CLOSE_BUTTON)
        self._wait_overlay_to_disappear()
