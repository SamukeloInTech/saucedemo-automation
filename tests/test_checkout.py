import pytest
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from test_data import (
    VALID_USERNAME,
    VALID_PASSWORD,
    BACKPACK,
    CHECKOUT_FIRST_NAME,
    CHECKOUT_LAST_NAME,
    CHECKOUT_POSTAL_CODE,
)


def _go_to_checkout(driver, product_name=BACKPACK):
    """Helper: log in, add a product, and reach the checkout form page."""
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login(VALID_USERNAME, VALID_PASSWORD)
    login_page.wait_for_inventory_page()

    products_page = ProductsPage(driver)
    products_page.add_to_cart(product_name)
    products_page.go_to_cart()

    cart_page = CartPage(driver)
    cart_page.click_checkout()


@pytest.mark.regression
@pytest.mark.checkout
def test_checkout_form_shows(driver):
    _go_to_checkout(driver)
    checkout_page = CheckoutPage(driver)

    assert checkout_page.get_title() == "Checkout: Your Information"


@pytest.mark.smoke
@pytest.mark.checkout
def test_successful_checkout(driver):
    _go_to_checkout(driver)
    checkout_page = CheckoutPage(driver)

    checkout_page.fill_form(CHECKOUT_FIRST_NAME, CHECKOUT_LAST_NAME, CHECKOUT_POSTAL_CODE)
    checkout_page.click_continue()

    assert checkout_page.get_total().startswith("Total: $")

    checkout_page.click_finish()

    assert checkout_page.get_confirmation_message() == "Thank you for your order!"


@pytest.mark.regression
@pytest.mark.checkout
def test_checkout_total_is_correct(driver):
    _go_to_checkout(driver)
    checkout_page = CheckoutPage(driver)

    checkout_page.fill_form(CHECKOUT_FIRST_NAME, CHECKOUT_LAST_NAME, CHECKOUT_POSTAL_CODE)
    checkout_page.click_continue()

    total_text = checkout_page.get_total()
    total_value = float(total_text.split("$")[1])
    assert total_value >= 29.99