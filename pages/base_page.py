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

    MODAL_OVERLAY = (By.CLASS_NAME, "Modal_modal_overlay__x2ZCr")

    @allure.step("Дождаться окончания лоадера")
    def _wait_overlay_to_disappear(self):
        short_wait = WebDriverWait(self.driver, 2)
        try:
            short_wait.until(EC.visibility_of_element_located(self.MODAL_OVERLAY))
            self.wait.until(EC.invisibility_of_element_located(self.MODAL_OVERLAY))
        except TimeoutException:
            pass

    @allure.step("Проверить отображение элемента, по локатору: {locator}")
    def _is_visible(self, locator) -> bool:
        try:
            self.wait.until(EC.visibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False

    @allure.step("Нажать на элемент по локатору: {locator}")
    def _click(self, locator):
        self._wait_overlay_to_disappear()
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    @allure.step("Получить текст по локатору: {locator}")
    def _get_text(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator)).text

    @allure.step("Получить текст из атрибура 'value' по локатору: {locator}")
    def _get_value(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator)).get_attribute("value")

    @allure.step("Ввести текст: {text} в поле, по локатору: {locator}")
    def _send_keys(self, locator, text):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.clear()
        element.send_keys(text)

    @allure.step("Получить значение атрибута '{attribute}' по локатору {locator}")
    def _get_attribute_value(self, locator, attribute: str):
        return self.wait.until(EC.visibility_of_element_located(locator)).get_attribute(attribute)

    @allure.step("Получить текущую ссылку")
    def _get_current_url(self):
        return self.driver.current_url
