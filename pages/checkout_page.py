from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage:
    # Locators
    TITLE = (By.CSS_SELECTOR, "[data-test='title']")
    FIRST_NAME = (By.CSS_SELECTOR, "[data-test='firstName']")
    LAST_NAME = (By.CSS_SELECTOR, "[data-test='lastName']")
    POSTAL_CODE = (By.CSS_SELECTOR, "[data-test='postalCode']")
    CONTINUE_BUTTON = (By.CSS_SELECTOR, "[data-test='continue']")
    FINISH_BUTTON = (By.CSS_SELECTOR, "[data-test='finish']")
    TOTAL_LABEL = (By.CSS_SELECTOR, "[data-test='total-label']")
    COMPLETE_HEADER = (By.CSS_SELECTOR, "[data-test='complete-header']")

    def __init__(self, driver):
        self.driver = driver

    def get_title(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.TITLE)
        )
        return self.driver.find_element(*self.TITLE).text

    def fill_form(self, first_name, last_name, postal_code):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.FIRST_NAME)
        )
        self.driver.find_element(*self.FIRST_NAME).send_keys(first_name)
        self.driver.find_element(*self.LAST_NAME).send_keys(last_name)
        self.driver.find_element(*self.POSTAL_CODE).send_keys(postal_code)

    def click_continue(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.CONTINUE_BUTTON)
        ).click()

    def click_finish(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.FINISH_BUTTON)
        ).click()

    def get_total(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.TOTAL_LABEL)
        )
        return self.driver.find_element(*self.TOTAL_LABEL).text

    def get_confirmation_message(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.COMPLETE_HEADER)
        )
        return self.driver.find_element(*self.COMPLETE_HEADER).text