import pytest
from selenium import webdriver


@pytest.fixture
def driver(request):
    browser = webdriver.Chrome()
    yield browser

    if request.node.rep_call.failed:
        browser.save_screenshot(f"screenshots/{request.node.name}.png")

    browser.quit()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)