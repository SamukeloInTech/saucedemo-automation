from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage:
    # Locators
    TITLE = (By.CSS_SELECTOR, "[data-test='title']")
    ITEM_NAME = (By.CSS_SELECTOR, "[data-test='inventory-item-name']")
    ITEM_PRICE = (By.CSS_SELECTOR, "[data-test='inventory-item-price']")

    def __init__(self, driver):
        self.driver = driver

    def get_title(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.TITLE)
        )
        return self.driver.find_element(*self.TITLE).text

    def get_item_name(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.ITEM_NAME)
        )
        return self.driver.find_element(*self.ITEM_NAME).text

    def get_item_price(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.ITEM_PRICE)
        )
        return self.driver.find_element(*self.ITEM_PRICE).text

    def remove_item(self, product_name):
        slug = product_name.lower().replace(" ", "-")
        locator = (By.CSS_SELECTOR, f"[data-test='remove-{slug}']")
        WebDriverWait(self.driver, 10).until(
        EC.element_to_be_clickable(locator)
       ).click()
        # Wait until the item is actually gone from the page
        WebDriverWait(self.driver, 10).until(
        EC.invisibility_of_element_located(self.ITEM_NAME)
    )

    def click_checkout(self):
        locator = (By.CSS_SELECTOR, "[data-test='checkout']")
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(locator)
        ).click()