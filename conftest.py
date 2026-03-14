import allure
import pytest
from selenium import webdriver

from helpers.api_client import create_user, delete_user
from pages.account_profile_page import AccountProfilePage
from pages.forgot_password_page import ForgotPasswordPage
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.order_feed_page import OrderFeedPage
from pages.reset_password_page import ResetPasswordPage
from utils.attach import attach_screenshot


@pytest.fixture(scope="function", autouse=True, params=["firefox", "chrome"])
def browser(request):
    if request.param == "firefox":
        driver = webdriver.Firefox()
    elif request.param == "chrome":
        driver = webdriver.Chrome()
    else:
        raise ValueError(f"Неизвестный браузер: {request.param}")

    driver.maximize_window()
    yield driver

    attach_screenshot(driver)
    driver.quit()


@pytest.fixture
def main_page(browser):
    return MainPage(browser)


@pytest.fixture
def login_page(browser):
    return LoginPage(browser)


@pytest.fixture
def forgot_password_page(browser):
    return ForgotPasswordPage(browser)


@pytest.fixture
def reset_password_page(browser):
    return ResetPasswordPage(browser)


@pytest.fixture
def account_profile_page(browser):
    return AccountProfilePage(browser)


@pytest.fixture
def order_feed_page(browser):
    return OrderFeedPage(browser)


@pytest.fixture
def created_user():
    response_create_user = create_user()
    created_user_data = response_create_user.user_data
    created_user_token = response_create_user.token

    yield created_user_data

    delete_user(created_user_token)


@pytest.fixture
def user_is_auth(login_page, created_user):
    login_page.open()

    email = created_user["email"]
    password = created_user["password"]
    name = created_user["name"]

    login_page.auth(email, password)

    yield email, name


@pytest.fixture
def created_order(user_is_auth, main_page):
    main_page.drag_first_ingredient_to_constructor()
    main_page.drag_third_ingredient_to_constructor()
    main_page.click_order_button()
    order_number = main_page.get_order_modal_number()
    main_page.close_order_confirmation_modal()

    yield order_number


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Хук, который отлавливает момент падения теста и делает скриншот.
    Необходим, чтобы успеть сделать скриншот, если на экране, к примеру
    помешал поп-ап, на странице не видно необходимый элемент или элемент не отобразился и т.п.
    """

    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        driver = item.funcargs.get("browser")
        if driver:
            with allure.step("Скриншот при падении"):
                attach_screenshot(driver)
