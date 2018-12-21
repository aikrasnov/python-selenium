from src.pages.main_page import MainPage
from src.wait.conditions import CONDITIONS
import pytest


@pytest.mark.parametrize("text", ["!@#$%^"])
@pytest.allure.testcase("http://test-tracker/suggest-4")
@pytest.allure.feature("SUGGEST-4: Саджест. Спецсимволы")
def test_suggest_4(driver, text):
    page = MainPage(driver)
    page.open()

    input_text = text
    message = "как минимум один специальный символ !@#$%^&*?_~+=."

    with pytest.allure.step("suggest should not be visible"):
        page.check_suggest_not_visible()
    with pytest.allure.step(f"should type text {input_text}"):
        page.enter_query(input_text)
    with pytest.allure.step(f"should have message {message}"):
        page.check_suggest_text(CONDITIONS.equal, message)
