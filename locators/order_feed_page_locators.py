from selenium.webdriver.common.by import By

FIRST_ORDER_CARD = (By.XPATH, "(//a[contains(@class, 'OrderHistory')])[1]")
ORDER_DETAILS_MODAL = (By.XPATH, "//div[contains(@class, 'Modal_orderBox')]")
ORDER_NUMBERS_IN_FEED = (By.XPATH, "//p[contains(text(), '#')]")
ALL_TIME_COUNTER = (By.XPATH, "(//p[contains(@class, 'OrderFeed_number')])[1]")
TODAY_COUNTER = (By.XPATH, "(//p[contains(@class, 'OrderFeed_number')])[2]")
IN_PROGRESS_ORDER_NUMBERS = (By.XPATH, "//ul[contains(@class, 'OrderFeed_orderListReady')]//li")