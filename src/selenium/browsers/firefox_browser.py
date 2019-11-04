from src.selenium.browsers.abstract_browser import AbstractBrowser
from src.selenium.browsers.available_browsers import AvailableBrowsers
from selenium.webdriver import Firefox, Remote

_DEFAULT_FIREFOX_CAPS = {"pageLoadStrategy": "eager", "browserName": AvailableBrowsers.FIREFOX, "version": "64.0"}


class FirefoxBrowser(AbstractBrowser):
    def __init__(self):
        self._set_browser_name(AvailableBrowsers.FIREFOX)
        super().__init__()

    def create_driver_instance(self) -> Firefox:
        if self.is_local_browser():
            return Firefox(capabilities=self._capabilities_to_dict())

        return Remote(desired_capabilities=self._capabilities_to_dict(),
                      command_executor=self.capabilities.command_executor)
