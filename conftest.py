import os
import pytest
import datetime
from selenium import webdriver

AVAILABLE_BROWSERS = {
    "chrome": "chrome",
    "firefox": "firefox"
}


@pytest.fixture(scope="function")
def driver(request, param):
    browser_type = request.config.getoption("--browser") or param
    save_screen = request.config.getoption("--screenonfail") or param

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
        if has_sauce_lab:
            caps.update({"browserName": "firefox", "platform": "Windows 10", "version": "64.0"})
            browser = webdriver.Remote(desired_capabilities=caps, command_executor=command_executor)
        else:
            browser = webdriver.Firefox(desired_capabilities=caps)

    else:
        raise RuntimeError(f"Unknown browser ${browser_type}")

    yield browser

    if request.node.rep_call.failed and save_screen:
        screenshots_path = f"./screenshots/{browser_type}/{request.node.name}/"
        if not os.path.exists(screenshots_path):
            os.makedirs(screenshots_path)

        now = datetime.datetime.now()
        browser.save_screenshot(f"{screenshots_path}{now.day}-{now.month}-{now.year}.png")

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
                     action="store_true",
                     help="Run tests in all available browsers")

    parser.addoption("--screenonfail",
                     default=False,
                     action="store_true",
                     help="Save screenshot on test fail")


def pytest_generate_tests(metafunc):
    if metafunc.config.getoption("allbrowsers") and not metafunc.config.getoption("browser"):
        metafunc.parametrize("param", AVAILABLE_BROWSERS.keys())


# https://automated-testing.info/t/pytest-krivo-otobrazhaet-kejsy-parametrizaczii-na-russkom/17908
def pytest_make_parametrize_id(config, val):
    return repr(val)


# https://docs.pytest.org/en/latest/example/simple.html#making-test-result-information-available-in-fixtures
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # execute all other hooks to obtain the report object
    outcome = yield
    rep = outcome.get_result()

    # set a report attribute for each phase of a call, which can
    # be "setup", "call", "teardown"

    setattr(item, "rep_" + rep.when, rep)
