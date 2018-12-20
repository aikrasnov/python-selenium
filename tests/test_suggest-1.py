from src.pages.main_page import GoMailRu
import pytest


@pytest.mark.parametrize("text", ["foobar", "бесплатно", "без регистрации"])
@pytest.allure.testcase("http://test-tracker/suggest-1")
def test_suggest_1(driver, text):
    page = GoMailRu(driver)

    input_text = text

    with pytest.allure.step("suggest should not be visible"):
        page.check_suggest_not_visible()
    with pytest.allure.step(f"should type text {input_text}"):
        page.enter_query(input_text)
    with pytest.allure.step("suggest should be visible"):
        page.check_suggest_visible()
    with pytest.allure.step(f"suggest should have text {input_text}"):
        page.check_suggest_text(input_text)
    with pytest.allure.step("should clear search field"):
        page.clear_query()
    with pytest.allure.step("suggest should disappear"):
        page.check_suggest_not_visible()
