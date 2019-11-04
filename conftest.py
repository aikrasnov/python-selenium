import os
import pytest
import datetime

from config.config import Config
from src.selenium.browser_factory import BrowserFactory
from src.selenium.browsers.available_browsers import AvailableBrowsers
from src.selenium.capabilities import Capabilities


@pytest.fixture(scope="class")
def driver(request, param):
    # use param if its parametrized run
    browser_type = Config.browser or param
    save_screen = Config.browser

    capabilities = Capabilities(browser_type, version="", page_load_strategy="none")

    if Config.has_saucelabs_connect:
        command_executor = Config.saucelabs_connection_string
        capabilities.set_capability(Capabilities.command_executor, command_executor)

    browser = BrowserFactory.get_driver(capabilities)
    yield browser

    if request.node.rep_call.failed and save_screen:
        screenshots_path = f"./screenshots/{browser_type}/{request.node.name}/"
        if not os.path.exists(screenshots_path):
            os.makedirs(screenshots_path)

        now = datetime.datetime.now()
        browser.save_screenshot(f"{screenshots_path}{now.day}-{now.month}-{now.year}.png")

    browser.quit()


@pytest.fixture(scope="class")
def param(request):
    # we don"t have request.param when not parametrize tests with pytest_generate_tests
    try:
        return request.param
    except AttributeError:
        pass


def pytest_addoption(parser):
    parser.addoption("--browser",
                     action="append",
                     help=f"Browser. Valid options are {AvailableBrowsers.get_available_browsers()}")

    parser.addoption("--all_browsers",
                     default=False,
                     action="store_true",
                     help="Run tests in all available browsers")

    parser.addoption("--browser_version",
                     default="Windows",
                     action="store_true",
                     help="Browsers version for run tests")

    parser.addoption("--platform",
                     default="Windows",
                     action="store_true",
                     help="OS where run tests")

    parser.addoption("--screen_on_fail",
                     default=False,
                     action="store_true",
                     help="Save screenshot on test fail")

    parser.addoption("--base_url",
                     default="https://go.mail.ru/",
                     action="store_true",
                     help="base url for tests")


def pytest_configure(config):
    Config.setup({
        "base_url": config.getoption("--base_url"),
        "screen_on_fail": config.getoption("--screen_on_fail"),
        "browser": config.getoption("--browser"),
        "all_browsers": config.getoption("--all_browsers"),
        "browser_version": config.getoption("--browser_version"),
        "platform": config.getoption("--platform"),
    })


def pytest_generate_tests(metafunc):
    if Config.all_browser and not Config.browser:
        metafunc.parametrize("param", AvailableBrowsers.get_available_browsers())


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
