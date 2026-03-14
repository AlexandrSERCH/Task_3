from selenium.webdriver.common.by import By

NAME_FIELD = (By.CSS_SELECTOR, "input[name='Name']")
LOGIN_FIELD = (By.CSS_SELECTOR, "input[type='text'][name='name']")
ORDER_HISTORY_LINK = (By.XPATH, "//a[text()='История заказов']")
LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выход']")
FIRST_ORDER_NUMBER = (By.XPATH, "(//p[contains(text(), '#')])[1]")
