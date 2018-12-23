from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.remote.webdriver import WebDriver
from src.wait.conditions import CONDITIONS


class Wait(object):
    def __init__(self, browser: WebDriver, timeout=10):
        self.__browser = browser
        self.__timeout = timeout
        self.__wait = WebDriverWait(self.__browser, self.__timeout)

    def __wait_until(self, fn):
        # не смотря на ошибки, пытаемся дождаться появления элемента
        def safe_wait(wait_function, browser):
            try:
                return wait_function(browser)
            except (StaleElementReferenceException, NoSuchElementException) as exc:
                return False

        self.__wait.until(lambda browser: safe_wait(fn, browser))

    def wait_until_visible_by_xpath_locator(self, selector: str):
        self.__wait_until(lambda browser: browser.find_element_by_xpath(selector).is_displayed())

    def wait_until_visible_by_css_selector(self, selector: str):
        self.__wait_until(lambda browser: browser.find_element_by_css_selector(selector).is_displayed())

    def wait_until_not_visible_by_css_selector(self, selector: str):
        self.__wait_until((lambda browser: not browser.find_element_by_css_selector(selector).is_displayed()))

    def wait_elements_count_by_css_selector(self, selector: str, condition: str, count: int):
        if condition == CONDITIONS.equal:
            self.__wait_until(lambda browser: len(browser.find_elements_by_css_selector(selector)) == count)
        else:
            raise RuntimeError(f"Unknown condition {condition}")
