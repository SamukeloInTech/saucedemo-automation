from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ProductsPage:
    # Locators
    TITLE = (By.CSS_SELECTOR, "[data-test='title']")
    CART_LINK = (By.CSS_SELECTOR, "[data-test='shopping-cart-link']")
    CART_BADGE = (By.CSS_SELECTOR, "[data-test='shopping-cart-badge']")

    def __init__(self, driver):
        self.driver = driver

    def get_title(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.TITLE)
        )
        return self.driver.find_element(*self.TITLE).text

    def add_to_cart(self, product_name):
        slug = product_name.lower().replace(" ", "-")
        locator = (By.CSS_SELECTOR, f"[data-test='add-to-cart-{slug}']")
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(locator)
        ).click()

    def get_cart_count(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.CART_BADGE)
        )
        return int(self.driver.find_element(*self.CART_BADGE).text)

    def go_to_cart(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.CART_LINK)
        ).click()