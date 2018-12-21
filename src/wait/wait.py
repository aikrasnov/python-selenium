from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.remote.webdriver import WebDriver
from src.wait.conditions import CONDITIONS


class Wait(object):
    def __init__(self, browser: WebDriver, timeout=10):
        self.__browser = browser
        self.__timeout = timeout
        self.__wait = WebDriverWait(self.__browser, self.__timeout)

    def wait_until_visible_by_xpath_locator(self, selector: str):
        self.__wait.until(lambda browser: browser.find_element_by_xpath(selector).is_displayed())

    def wait_until_visible_by_css_selector(self, selector: str):
        self.__wait.until(lambda browser: browser.find_element_by_css_selector(selector).is_displayed())

    def wait_until_not_visible_by_css_selector(self, selector: str):
        self.__wait.until(lambda browser: not browser.find_element_by_css_selector(selector).is_displayed())

    def wait_elements_count_by_css_selector(self, selector: str, condition: str, count: int):
        if condition == CONDITIONS.equal:
            self.__wait.until(lambda browser: len(browser.find_elements_by_css_selector(selector)) == count)
        else:
            raise RuntimeError(f"Unknown condition {condition}")
