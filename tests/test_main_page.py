import allure


@allure.epic("Главная страница")
@allure.feature("Навигация")
class TestMainPageNavigation:

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.tag("UI", "regress", "Навигация")
    @allure.title("Переход по клику на 'Конструктор' из личного кабинета")
    def test_redirect_to_constructor_from_account(self, user_is_auth, main_page):
        main_page.click_account_button_in_header()
        main_page.click_constructor_button_in_header()

        main_page.success_visible_constructor_title()

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.tag("UI", "regress", "Навигация")
    @allure.title("Переход по клику на 'Лента заказов'")
    def test_redirect_to_order_feed_from_account(self, user_is_auth, main_page):
        main_page.click_order_feed_button_in_header()

        assert "feed" in main_page.get_current_url()
        main_page.success_visible_order_feed_title()


@allure.epic("Главная страница")
@allure.feature("Работа с ингредиентами")
class TestIngredients:

    @allure.severity(allure.severity_level.NORMAL)
    @allure.tag("UI", "regress", "Ингредиенты")
    @allure.title("Клик на ингредиент открывает модальное окно с деталями")
    def test_ingredient_modal_appears_on_click(self, main_page):
        main_page.open()
        ingredient_name = main_page.get_first_ingredient_name()
        main_page.click_first_ingredient()

        main_page.success_visible_ingredient_modal()

        with allure.step("Успешное отображение названия ингридиента в модальном окне"):
            modal_name = main_page.get_ingredient_modal_name()
            assert ingredient_name == modal_name

    @allure.severity(allure.severity_level.NORMAL)
    @allure.tag("UI", "regress", "Ингредиенты")
    @allure.title("При добавлении ингредиента в заказ увеличивается счётчик")
    def test_ingredient_counter_increases_on_add(self, main_page):
        main_page.open()
        assert main_page.get_third_ingredient_counter() == 0

        main_page.drag_third_ingredient_to_constructor()

        with allure.step("Успешное увелечение счётчика"):
            assert main_page.get_third_ingredient_counter() == 1

        main_page.drag_third_ingredient_to_constructor()

        with allure.step("Успешное увелечение счётчика"):
            assert main_page.get_third_ingredient_counter() == 2

    @allure.severity(allure.severity_level.NORMAL)
    @allure.tag("UI", "regress", "Ингредиенты")
    @allure.title("Закрытие модального окна кликом по крестику")
    def test_ingredient_modal_closes_on_close_button(self, main_page):
        main_page.open()
        main_page.click_first_ingredient()
        main_page.click_close_ingredient_modal()

        main_page.success_invisible_ingredient_modal()


@allure.epic("Главная страница")
@allure.feature("Оформление заказа")
class TestOrder:

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.tag("UI", "regress", "Заказ")
    @allure.title("Залогиненный пользователь может оформить заказ")
    def test_authenticated_user_can_place_order(self, user_is_auth, main_page):
        main_page.drag_first_ingredient_to_constructor()
        main_page.drag_third_ingredient_to_constructor()
        main_page.click_order_button()

        order_number = int(main_page.get_order_modal_number())
        assert order_number > 9999

        with allure.step("Успешное отображение модального окна об оформлении заказа"):
            actual_text_in_order_modal = main_page.get_order_modal_text()
            assert "Ваш заказ начали готовить" in actual_text_in_order_modal
