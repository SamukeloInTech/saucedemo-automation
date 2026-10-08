import pytest
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from test_data import VALID_USERNAME, VALID_PASSWORD, BACKPACK, BIKE_LIGHT


def _login(driver):
    """Helper to log in before each products test."""
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login(VALID_USERNAME, VALID_PASSWORD)
    login_page.wait_for_inventory_page()


@pytest.mark.smoke
@pytest.mark.products
def test_products_page_loads(driver):
    _login(driver)
    products_page = ProductsPage(driver)

    assert products_page.get_title() == "Products"


@pytest.mark.smoke
@pytest.mark.products
def test_add_one_product_to_cart(driver):
    _login(driver)
    products_page = ProductsPage(driver)

    products_page.add_to_cart(BACKPACK)

    assert products_page.get_cart_count() == 1


@pytest.mark.regression
@pytest.mark.products
def test_add_two_products_to_cart(driver):
    _login(driver)
    products_page = ProductsPage(driver)

    products_page.add_to_cart(BACKPACK)
    products_page.add_to_cart(BIKE_LIGHT)

    assert products_page.get_cart_count() == 2