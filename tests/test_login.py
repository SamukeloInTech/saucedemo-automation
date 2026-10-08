import pytest
from pages.login_page import LoginPage
from test_data import VALID_USERNAME, VALID_PASSWORD, LOCKED_OUT_USERNAME


@pytest.mark.smoke
@pytest.mark.login
def test_valid_login(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login(VALID_USERNAME, VALID_PASSWORD)

    login_page.wait_for_inventory_page()
    assert "inventory" in driver.current_url


@pytest.mark.regression
@pytest.mark.login
@pytest.mark.parametrize("username, password, expected_error", [
    (VALID_USERNAME, "wrong_password", "Username and password do not match"),
    ("", VALID_PASSWORD, "Username is required"),
    (VALID_USERNAME, "", "Password is required"),
    (LOCKED_OUT_USERNAME, VALID_PASSWORD, "Sorry, this user has been locked out"),
])
def test_invalid_login(driver, username, password, expected_error):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login(username, password)

    assert expected_error in login_page.get_error_message()