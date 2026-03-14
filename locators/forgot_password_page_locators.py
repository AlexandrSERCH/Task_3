from selenium.webdriver.common.by import By

FORGOT_PASSWORD_TITLE = (By.CSS_SELECTOR, "main h2")
EMAIL_INPUT = (By.CSS_SELECTOR, "input[name='name']")
RECOVERY_BUTTON = (By.XPATH, "//button[text()='Восстановить']")