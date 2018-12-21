from src.pages.main_page import MainPage
import pytest


@pytest.mark.parametrize("text", ["@@@@@"])
@pytest.allure.testcase("http://test-tracker/suggest-2")
@pytest.allure.feature("SUGGEST-2: Саджест не должен появляться")
def test_suggest_2(driver, text):
    page = MainPage(driver)
    page.open()

    input_text = text

    with pytest.allure.step("suggest should not be visible"):
        page.check_suggest_not_visible()
    with pytest.allure.step(f"should type text {input_text}"):
        page.enter_query(input_text)
    with pytest.allure.step("suggest should not be visible"):
        page.check_suggest_not_visible_with_timeout()
