from typing import List, Type, Union
from src.selenium.browsers.chrome_browser import ChromeBrowser
from src.selenium.browsers.firefox_browser import FirefoxBrowser


class AvailableBrowsers(object):
    CHROME = 'chrome'
    FIREFOX = 'firefox'

    @classmethod
    def get_available_browsers(cls) -> List[str]:
        available_browsers = []

        for attribute in dir(AvailableBrowsers):
            if not attribute.startswith("__") and not callable(getattr(AvailableBrowsers, attribute)):
                available_browsers.append(attribute)

        return available_browsers

    @staticmethod
    def get_available_browser_constructors() -> List[Type[Union[ChromeBrowser, FirefoxBrowser]]]:
        return [ChromeBrowser, FirefoxBrowser]
