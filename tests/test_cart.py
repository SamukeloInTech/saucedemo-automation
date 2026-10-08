import pytest
from selenium.webdriver.common.by import By
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from test_data import VALID_USERNAME, VALID_PASSWORD, BACKPACK, BACKPACK_PRICE


def _login_and_add_item(driver, product_name):
    """Helper: log in and add one product to the cart."""
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login(VALID_USERNAME, VALID_PASSWORD)
    login_page.wait_for_inventory_page()

    products_page = ProductsPage(driver)
    products_page.add_to_cart(product_name)


@pytest.mark.smoke
@pytest.mark.cart
def test_cart_shows_added_item(driver):
    _login_and_add_item(driver, BACKPACK)

    products_page = ProductsPage(driver)
    products_page.go_to_cart()

    cart_page = CartPage(driver)
    assert cart_page.get_title() == "Your Cart"
    assert cart_page.get_item_name() == BACKPACK


@pytest.mark.regression
@pytest.mark.cart
def test_cart_shows_correct_price(driver):
    _login_and_add_item(driver, BACKPACK)

    products_page = ProductsPage(driver)
    products_page.go_to_cart()

    cart_page = CartPage(driver)
    assert cart_page.get_item_price() == BACKPACK_PRICE


@pytest.mark.regression
@pytest.mark.cart
def test_remove_item_from_cart(driver):
    _login_and_add_item(driver, BACKPACK)

    products_page = ProductsPage(driver)
    products_page.go_to_cart()

    cart_page = CartPage(driver)
    cart_page.remove_item(BACKPACK)

    items = driver.find_elements(By.CSS_SELECTOR, "[data-test='inventory-item-name']")
    assert len(items) == 0