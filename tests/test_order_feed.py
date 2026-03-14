import allure


@allure.epic("Лента заказов")
@allure.feature("Детали заказа")
class TestOrderFeedDetails:

    @allure.severity(allure.severity_level.NORMAL)
    @allure.tag("UI", "regress", "Лента заказов")
    @allure.title("Клик на заказ открывает всплывающее окно с деталями")
    def test_order_details_modal_appears_on_click(self, main_page, order_feed_page):
        main_page.open()
        main_page.click_order_feed_button_in_header()

        order_feed_page.click_first_order()

        order_feed_page.success_visible_order_details_modal()


@allure.epic("Лента заказов")
@allure.feature("Счётчики заказов")
class TestOrderFeedCounters:

    @allure.severity(allure.severity_level.NORMAL)
    @allure.tag("UI", "regress", "Лента заказов")
    @allure.title("При создании нового заказа счётчик 'Выполнено за все время' и 'Выполнено за сегодня' увеличивается")
    def test_counters_increase_after_order(self, user_is_auth, main_page, order_feed_page):
        order_feed_page.open()
        all_time_before = order_feed_page.get_all_time_counter()
        today_before = order_feed_page.get_today_counter()

        main_page.open()
        main_page.drag_first_ingredient_to_constructor()
        main_page.drag_third_ingredient_to_constructor()
        main_page.click_order_button()
        main_page.close_order_confirmation_modal()
        order_feed_page.open()

        assert order_feed_page.get_all_time_counter() > all_time_before
        assert order_feed_page.get_today_counter() > today_before


@allure.epic("Лента заказов")
@allure.feature("Заказы пользователя в ленте")
class TestUserOrdersInFeed:

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.tag("UI", "regress", "Лента заказов")
    @allure.title("Заказы из 'Истории заказов' отображаются в 'Ленте заказов'")
    def test_orders_from_history_appear_in_feed(self, created_order, main_page, account_profile_page, order_feed_page):
        main_page.click_account_button_in_header()
        account_profile_page.click_order_history()
        first_order_number = account_profile_page.get_first_order_number()

        order_feed_page.open()
        feed_order_numbers = order_feed_page.get_all_order_numbers()

        assert first_order_number in feed_order_numbers

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.tag("UI", "regress", "Лента заказов")
    @allure.title("После оформления заказа его номер появляется в разделе 'В работе'")
    def test_order_number_appears_in_progress(self, user_is_auth, main_page, order_feed_page):
        main_page.drag_first_ingredient_to_constructor()
        main_page.drag_third_ingredient_to_constructor()
        main_page.click_order_button()
        order_number = main_page.get_order_modal_number()

        order_feed_page.open()

        assert order_feed_page.wait_for_order_in_progress(order_number)