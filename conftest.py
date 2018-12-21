import os
import pytest
from selenium import webdriver

AVAILABLE_BROWSERS = {
    "chrome": "chrome",
    "firefox": "firefox"
}


@pytest.fixture(scope="function")
def driver(request, param):
    browser_type = request.config.getoption("--browser") or param

    username = None
    access_key = None

    try:
        username = os.environ["SAUCE_USERNAME"]
        access_key = os.environ["SAUCE_ACCESS_KEY"]
    except KeyError:
        pass

    has_sauce_lab = username and access_key
    caps = {}
    command_executor = f"https://{username}:{access_key}@ondemand.saucelabs.com/wd/hub"

    if AVAILABLE_BROWSERS["chrome"] in browser_type:
        # use "none" only for Chrome, because there some trouble in geckrodriver with this strategy
        caps.update({"pageLoadStrategy": "none"})
        if has_sauce_lab:
            caps.update({"browserName": "chrome", "platform": "Windows 10", "version": "71.0"})
            browser = webdriver.Remote(desired_capabilities=caps, command_executor=command_executor)
        else:
            browser = webdriver.Chrome(desired_capabilities=caps)

    elif AVAILABLE_BROWSERS["firefox"] in browser_type:
        # caps.update({"pageLoadStrategy": "normal"})
        if has_sauce_lab:
            caps.update({"browserName": "firefox", "platform": "Windows 10", "version": "64.0"})
            browser = webdriver.Remote(desired_capabilities=caps, command_executor=command_executor)
        else:
            browser = webdriver.Firefox(desired_capabilities=caps)

    else:
        raise RuntimeError(f"Unknown browser ${browser_type}")

    yield browser
    browser.quit()


@pytest.fixture(scope="function")
def param(request):
    # we don"t have request.param when not parametrize tests with pytest_generate_tests
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
    if metafunc.config.getoption("allbrowsers") and not metafunc.config.getoption("browser"):
        metafunc.parametrize("param", AVAILABLE_BROWSERS.keys())


# https://automated-testing.info/t/pytest-krivo-otobrazhaet-kejsy-parametrizaczii-na-russkom/17908
def pytest_make_parametrize_id(config, val):
    return repr(val)
