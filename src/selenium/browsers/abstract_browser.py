from src.selenium.capabilities import Capabilities
from abc import ABC, abstractmethod

import typing


class AbstractBrowser(ABC):

    browser_name = None

    def __init__(self):
        self.capabilities: Capabilities = None
        self.browser_name: str = None

    def _capabilities_to_dict(self) -> dict:
        return self.capabilities.to_dictionary()

    @classmethod
    def _set_browser_name(cls, name: str) -> None:
        cls.browser_name = name

    @classmethod
    def get_browser_name(cls) -> str:
        return cls.browser_name

    def set_capability(self, caps: Capabilities = None) -> None:
        if caps:
            self.capabilities = caps

    def is_local_browser(self) -> bool:
        return bool(self.capabilities.command_executor)

    @abstractmethod
    def create_driver_instance(self) -> typing.NoReturn:
        """
        Each subclass of AbstractBrowser should implement this method. By design.
        """
        raise NotImplemented("init_driver not implemented")
