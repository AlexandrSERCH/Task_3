import allure

from constants import order_feed_url
from locators.order_feed_page_locators import (
    FIRST_ORDER_CARD, ORDER_DETAILS_MODAL, ORDER_NUMBERS_IN_FEED,
    ALL_TIME_COUNTER, TODAY_COUNTER, IN_PROGRESS_ORDER_NUMBERS,
)
from pages.base_page import BasePage


class OrderFeedPage(BasePage):

    @allure.step("Открыть страницу 'Лента заказов'")
    def open(self):
        self._open_page(order_feed_url())

    @allure.step("Кликнуть на первый заказ в ленте")
    def click_first_order(self):
        self._click(FIRST_ORDER_CARD)

    @allure.step("Проверить отображение модального окна с деталями заказа")
    def success_visible_order_details_modal(self):
        assert self._is_visible(ORDER_DETAILS_MODAL)

    @allure.step("Получить список номеров заказов в ленте")
    def get_all_order_numbers(self) -> list:
        return self._get_elements_texts(ORDER_NUMBERS_IN_FEED)

    @allure.step("Получить значение счётчика 'Выполнено за всё время'")
    def get_all_time_counter(self) -> int:
        return int(self._get_text(ALL_TIME_COUNTER))

    @allure.step("Получить значение счётчика 'Выполнено за сегодня'")
    def get_today_counter(self) -> int:
        return int(self._get_text(TODAY_COUNTER))

    @allure.step("Получить список номеров заказов в разделе 'В работе'")
    def get_in_progress_order_numbers(self) -> list:
        self.wait.until(
            lambda d: any(
                el.text and el.text != "Все текущие заказы готовы!"
                for el in d.find_elements(*IN_PROGRESS_ORDER_NUMBERS)
            )
        )
        return self._get_elements_texts(IN_PROGRESS_ORDER_NUMBERS)

    @allure.step("Ожидать появления заказа {order_number} в разделе 'В работе'")
    def wait_for_order_in_progress(self, order_number: str) -> bool:
        try:
            self.wait.until(
                lambda d: any(
                    order_number in el.text
                    for el in d.find_elements(*IN_PROGRESS_ORDER_NUMBERS)
                )
            )
            return True
        except Exception:
            return False
