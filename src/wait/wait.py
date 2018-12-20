from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.remote.webdriver import WebDriver


class Wait(object):
    def __init__(self, browser: WebDriver, timeout=10):
        self.__browser = browser
        self.__timeout = timeout
        self.__wait = WebDriverWait(self.__browser, self.__timeout)

    def wait_until_visible_by_css_selector(self, selector: str):
        self.__wait.until(lambda browser: browser.find_element_by_css_selector(selector).is_displayed())

    def wait_until_not_visible_by_css_selector(self, selector: str):
        self.__wait.until(lambda browser: not browser.find_element_by_css_selector(selector).is_displayed())
