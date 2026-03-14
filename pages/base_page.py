from asyncio import wait

import allure
from selenium.common import TimeoutException, StaleElementReferenceException
from selenium.webdriver.common.action_chains import ActionChains
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

    @allure.step("Нажать на элемент по локатору (без ожидания оверлея): {locator}")
    def _click_without_overlay_wait(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    @allure.step("Нажать на элемент через JS по локатору: {locator}")
    def _click_js(self, locator):
        element = self.wait.until(EC.presence_of_element_located(locator))
        self.driver.execute_script("arguments[0].click();", element)

    @allure.step("Нажать на элемент по локатору: {locator}")
    def _click(self, locator):
        self._wait_overlay_to_disappear()
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    @allure.step("Получить текст по локатору: {locator}")
    def _get_text(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator)).text

    @allure.step("Получить список текстов по локатору: {locator}")
    def _get_elements_texts(self, locator) -> list:
        for _ in range(5):
            try:
                elements = self.wait.until(EC.presence_of_all_elements_located(locator))
                return [el.text for el in elements]
            except StaleElementReferenceException:
                pass
        return []

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

    @allure.step("Проверить скрытие элемента по локатору: {locator}")
    def _is_invisible(self, locator) -> bool:
        try:
            self.wait.until(EC.invisibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False

    @allure.step("Получить значение счётчика по локатору: {locator}")
    def _get_counter_value(self, locator) -> int:
        try:
            text = self.wait.until(EC.visibility_of_element_located(locator)).text
            return int(text)
        except TimeoutException:
            return 0

    def _js_drag_and_drop(self, source, target):
        self.driver.execute_script("""
            function simulateDragDrop(sourceNode, targetNode) {
                const EVENT_TYPES = ['dragstart', 'dragenter', 'dragover', 'drop', 'dragend'];
                function createEvent(type) {
                    const event = document.createEvent('DragEvent');
                    event.initMouseEvent(type, true, true, window, 0, 0, 0, 0, 0,
                        false, false, false, false, 0, null);
                    Object.defineProperty(event, 'dataTransfer', {
                        value: (() => {
                            let data = {};
                            return {
                                setData(k, v) { data[k] = v; },
                                getData(k) { return data[k]; },
                                clearData() { data = {}; },
                                setDragImage() {}
                            };
                        })()
                    });
                    return event;
                }
                sourceNode.dispatchEvent(createEvent('dragstart'));
                targetNode.dispatchEvent(createEvent('dragenter'));
                targetNode.dispatchEvent(createEvent('dragover'));
                targetNode.dispatchEvent(createEvent('drop'));
                sourceNode.dispatchEvent(createEvent('dragend'));
            }
            simulateDragDrop(arguments[0], arguments[1]);
        """, source, target)

    @allure.step("Перетащить элемент {source_locator} в {target_locator}")
    def _drag_and_drop(self, source_locator, target_locator):
        source = self.wait.until(EC.visibility_of_element_located(source_locator))
        target = self.wait.until(EC.visibility_of_element_located(target_locator))
        self._js_drag_and_drop(source, target)

    @allure.step("Ожидать пока URL не перестанет содержать: {text}")
    def _wait_for_url_not_contains(self, text: str):
        self.wait.until(lambda d: text not in d.current_url)

    @allure.step("Получить текущую ссылку")
    def _get_current_url(self):
        return self.driver.current_url
