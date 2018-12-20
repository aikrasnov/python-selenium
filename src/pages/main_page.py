from selenium.webdriver.remote.webdriver import WebDriver
from src.wait.wait import Wait
from config.config import BASE_URL


class GoMailRu(object):
    def __init__(self, browser: WebDriver):
        self.__browser = browser
        self.__wait = Wait(self.__browser)
        self.__browser.get(BASE_URL)

        self.__query_input = "#q"
        self.__suggest_select = ".go-suggests__wrap"
        self.__suggest_select_item = ".go-suggests__item__text"

    def enter_query(self, query: str):
        self.__wait.wait_until_visible_by_css_selector(self.__query_input)
        self.__browser.find_element_by_css_selector(self.__query_input).click()
        self.__browser.find_element_by_css_selector(self.__query_input).send_keys(query)

    def check_suggest_visible(self):
        self.__wait.wait_until_visible_by_css_selector(self.__suggest_select)

    def check_suggest_not_visible(self):
        self.__wait.wait_until_not_visible_by_css_selector(self.__suggest_select)

    def check_suggest_text(self, text: str):
        self.__wait.wait_until_visible_by_css_selector(self.__suggest_select_item)
        elements = self.__browser.find_elements_by_css_selector(self.__suggest_select_item)
        for element in elements:
            assert text in element.text, f"suggest text should contain [{text}]"

    def clear_query(self):
        self.__wait.wait_until_visible_by_css_selector(self.__query_input)
        self.__browser.find_element_by_css_selector(self.__query_input).clear()
