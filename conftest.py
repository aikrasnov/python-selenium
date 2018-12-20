import pytest
from selenium import webdriver

AVAILABLE_BROWSERS = {
    "chrome": "chrome",
    "firefox": "firefox"
}


@pytest.fixture(scope="function")
def driver(request, param):
    browser_type = request.config.getoption("--browser") or param

    if AVAILABLE_BROWSERS["chrome"] in browser_type:
        browser = webdriver.Chrome()
    elif AVAILABLE_BROWSERS["firefox"] in browser_type:
        browser = webdriver.Firefox()
    else:
        raise RuntimeError(f"Unknown browser ${browser_type}")

    yield browser
    browser.quit()


@pytest.fixture(scope="function")
def param(request):
    # we don't have request.param when not parametrize tests with pytest_generate_tests
    try:
        return request.param
    except AttributeError:
        pass


def pytest_addoption(parser):
    parser.addoption("--browser",
                     action="append",
                     help=f"Browser. Valid options are {AVAILABLE_BROWSERS.keys()}")

    parser.addoption("--allbrowsers",
                     default=False,
                     help="Run tests in all available browsers")


def pytest_generate_tests(metafunc):
    if metafunc.config.getoption("allbrowsers"):
        metafunc.parametrize("param", AVAILABLE_BROWSERS.keys())
