from src.selenium.browsers.abstract_browser import AbstractBrowser
from src.selenium.browsers.available_browsers import AvailableBrowsers
from src.selenium.capabilities import Capabilities
from selenium.webdriver import Chrome, Remote


_DEFAULT_CHROME_CAPS = {"page_load_strategy": "none", "browser_name": AvailableBrowsers.CHROME, "version": "71.0"}


class ChromeBrowser(AbstractBrowser):
    def __init__(self):
        self.browser_name = AvailableBrowsers.CHROME
        self.capabilities = Capabilities(**_DEFAULT_CHROME_CAPS)
        super().__init__()

    def create_driver_instance(self) -> Chrome:
        if self.is_local_browser():
            return Chrome(desired_capabilities=self._capabilities_to_dict())

        return Remote(desired_capabilities=self._capabilities_to_dict(),
                      command_executor=self.capabilities.command_executor)
