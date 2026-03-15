from selenium.webdriver.common.by import By

CONSTRUCTOR_TITLE = (By.CSS_SELECTOR, "main h1")
ORDER_FEED_TITLE = (By.CSS_SELECTOR, "main h1")

FIRST_INGREDIENT_SELECTOR = "(//a[contains(@href, '/ingredient/')])[1]"
FIRST_INGREDIENT = (By.XPATH, FIRST_INGREDIENT_SELECTOR)
FIRST_INGREDIENT_NAME = (By.XPATH, f"{FIRST_INGREDIENT_SELECTOR}//p[contains(@class, 'ingredient__text')]")

THIRD_INGREDIENT_SELECTOR = "(//a[contains(@href, '/ingredient/')])[3]"
THIRD_INGREDIENT = (By.XPATH, THIRD_INGREDIENT_SELECTOR)
THIRD_INGREDIENT_COUNTER = (By.XPATH, f"{THIRD_INGREDIENT_SELECTOR}//p[contains(@class, 'counter')]")

CONSTRUCTOR_DROP_ZONE = (By.XPATH, "//span[@class='constructor-element__row']")

ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")
ORDER_MODAL_NUMBER = (By.XPATH, "//h2[contains(@class, 'modal__title')]")
ORDER_MODAL_TEXT = (By.XPATH, "//div[contains(@class, 'modal__textContainer')]")
ORDER_MODAL_CLOSE_BUTTON = (By.XPATH, "//section[contains(@class, 'modal_opened')]//button[contains(@class, 'modal__close')]")

INGREDIENT_MODAL = (By.XPATH, "//h2[text()='Детали ингредиента']/..")
INGREDIENT_MODAL_NAME = (By.XPATH, "//h2[text()='Детали ингредиента']/../p")
INGREDIENT_MODAL_CLOSE_BUTTON = (By.XPATH, "//section[contains(@class, 'modal_opened')]//button[contains(@class, 'modal__close')]")
