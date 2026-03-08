import allure
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 15)

    @allure.step("Открыть страницу по ссылке: {url}")
    def _open_page(self, url):
        return self.driver.get(url)

    @allure.step("Проверить отображение элемента, по локатору: {locator}")
    def _is_visible(self, locator) -> bool:
        try:
            self.wait.until(EC.visibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False

    @allure.step("Нажать на элемент по локатору: {locator}")
    def _click(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    @allure.step("Получить текст по локатору: {locator}")
    def _get_text(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator)).text

    @allure.step("Ввести текст: {text} в поле, по локатору: {locator}")
    def _send_keys(self, locator, text):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.clear()
        element.send_keys(text)

    @allure.step("Получить значение атрибута '{attribute}' по локатору {locator}")
    def _get_attribute_value(self, locator, attribute: str):
        return self.wait.until(EC.visibility_of_element_located(locator)).get_attribute(attribute)
