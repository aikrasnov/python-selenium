import pytest
from selenium import webdriver


@pytest.fixture(scope="session")
def chrome():
    chrome = webdriver.Chrome()
    yield chrome
    chrome.quit()
