import pytest
from selenium import webdriver

@pytest.fixture(scope = "session")
def browser():
    # step: 1 - SETUP function (before  your scope)
    driver = webdriver.Chrome("C:\dev\chromedriver.exe")
    driver.implicitly_wait(10)
    yield driver
    # TEARDOWN (after your scope)
    # step: 6 - closing the browser
    driver.quit()
