from selenium.webdriver.common.by import By

FORGOT_PASSWORD_TEXT_LINK = (By.XPATH, "//a[@href='/forgot-password']")
EMAIL_FIELD = (By.CSS_SELECTOR, "input[name='name']")
PASSWORD_FIELD = (By.CSS_SELECTOR, "input[type='password']")
LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")