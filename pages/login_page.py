from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from config import BASE_URL


class LoginPage:
    URL = BASE_URL

    # Locators
    USERNAME = (By.ID, "user-name")
    PASSWORD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "[data-test='error']")

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(self.URL)
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.USERNAME)
        )

    def login(self, username, password):
        self.driver.find_element(*self.USERNAME).send_keys(username)
        self.driver.find_element(*self.PASSWORD).send_keys(password)
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.LOGIN_BUTTON)
        ).click()

    def get_error_message(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.ERROR_MESSAGE)
        )
        return self.driver.find_element(*self.ERROR_MESSAGE).text

    def wait_for_inventory_page(self):
        WebDriverWait(self.driver, 10).until(
            EC.url_contains("inventory")
        )