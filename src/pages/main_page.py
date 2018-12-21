from selenium.webdriver.remote.webdriver import WebDriver
from src.wait.wait import Wait
from config.config import BASE_URL
from src.wait.conditions import CONDITIONS
from time import sleep


class MainPage(object):
    def __init__(self, browser: WebDriver):
        self.__url = BASE_URL
        self.__browser = browser
        self.__wait = Wait(self.__browser)

        self.__query_input = "#q"
        self.__suggest_select = ".go-suggests__wrap"
        self.__suggest_select_item = ".go-suggests__item__text"

    def open(self):
        self.__browser.get(self.__url)
        self.__wait.wait_until_visible_by_css_selector(self.__query_input)

    def enter_query(self, query: str):
        self.__wait.wait_until_visible_by_css_selector(self.__query_input)
        self.__browser.find_element_by_css_selector(self.__query_input).click()
        self.__browser.find_element_by_css_selector(self.__query_input).send_keys(query)

    def clear_query(self):
        self.__wait.wait_until_visible_by_css_selector(self.__query_input)
        self.__browser.find_element_by_css_selector(self.__query_input).clear()

    def check_suggest_visible(self):
        self.__wait.wait_until_visible_by_css_selector(self.__suggest_select)

    def check_suggest_not_visible(self):
        self.__wait.wait_until_not_visible_by_css_selector(self.__suggest_select)

    def check_suggest_not_visible_with_timeout(self, timeout=5):
        sleep(timeout)
        self.check_suggest_not_visible()

    def check_suggest_text(self, condition: str, text: str,):
        self.__wait.wait_until_visible_by_css_selector(self.__suggest_select_item)
        elements = self.__browser.find_elements_by_css_selector(self.__suggest_select_item)

        if condition == CONDITIONS.contains:
            for element in elements:
                assert text in element.text, f"suggest text should contain {text}"
        elif condition == CONDITIONS.equal:
            for element in elements:
                assert text == element.text, f"suggest text should be equal {text}, not {element.text}"
        else:
            raise RuntimeError(f"Unknown condition {condition}")

    def check_suggest_item_count(self, condition: str, count: int):
        self.__wait.wait_elements_count_by_css_selector(self.__suggest_select_item, condition, count)

    def get_suggest_item_text(self, position: str) -> str:
        self.__wait.wait_until_visible_by_css_selector(self.__suggest_select_item)
        texts = [el.text for el in self.__browser.find_elements_by_css_selector(self.__suggest_select_item)]

        if position == "first":
            return texts[0]
        elif position == "last":
            return texts[-1]
        else:
            raise RuntimeError(f"Unknown position {position}")

    def click_at_suggest_item(self, position):
        self.__wait.wait_until_visible_by_css_selector(self.__suggest_select_item)
        elements = self.__browser.find_elements_by_css_selector(self.__suggest_select_item)

        if position == "first":
            elements[0].click()
        elif position == "last":
            elements[-1].click()
        else:
            raise RuntimeError(f"Unknown position {position}")
