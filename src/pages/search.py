from selenium.webdriver.remote.webdriver import WebDriver
from src.wait.wait import Wait
from config.config import BASE_URL


class Search(object):
    def __init__(self, browser: WebDriver):
        self.url = BASE_URL + "search/"
        self.__browser = browser
        self.__wait = Wait(self.__browser)

        self.__search_input = "(//input[@type='text'])[1]"

    def check_search_input_text(self, input_text: str):
        self.__wait.wait_until_visible_by_xpath_locator(self.__search_input)
        text = self.__browser.find_element_by_xpath(self.__search_input).get_property("value")
        assert text == input_text, f"Text from input should be equal {text}"
