import pytest
import os  # Added this to create the screenshots folder automatically
from selenium import webdriver
from selenium.webdriver.chrome.options import Options  # Added this import

@pytest.fixture
def driver(request):
    # --- NEW CODE FOR GITHUB ACTIONS (CI/CD) ---
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")
    # -------------------------------------------

    # Pass the options into the Chrome driver
    browser = webdriver.Chrome(options=options) 
    
    yield browser

    if request.node.rep_call.failed:
        # Ensure the screenshots folder exists before trying to save
        os.makedirs("screenshots", exist_ok=True)
        browser.save_screenshot(f"screenshots/{request.node.name}.png")

    browser.quit()

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)