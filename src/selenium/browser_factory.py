from typing import Union
from src.selenium.browsers.available_browsers import AvailableBrowsers
from src.selenium.capabilities import Capabilities


class BrowserFactory(object):
    """Factory class for WebDriver"""

    def __init__(self):
        pass

    @staticmethod
    def get_driver(capabilities: Capabilities) -> Union[AvailableBrowsers.get_available_browser_constructors()]:
        browser_name = capabilities.get_capability(Capabilities.browser_name)

        if browser_name not in AvailableBrowsers.get_available_browsers():
            raise RuntimeError(f"Unknown browser name: {browser_name}")

        webdriver_constructor = None
        browser_constructors = AvailableBrowsers.get_available_browser_constructors()
        for constructor in browser_constructors:
            if browser_name == constructor.get_browser_name():
                webdriver_constructor = constructor
                break

        webdriver = webdriver_constructor()
        webdriver.set_capability(capabilities)
        return webdriver.create_driver_instance()
