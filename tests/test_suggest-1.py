from src.pages.main_page import GoMailRu
import pytest


@pytest.mark.parametrize('text', ['foobar', 'бесплатно', 'без регистрации'])
def test_suggest_1(driver, text):
    print(driver)
    page = GoMailRu(driver)

    input_text = text

    page.check_suggest_not_visible()
    page.enter_query(input_text)
    page.check_suggest_visible()
    page.check_suggest_text(input_text)
    page.clear_query()
    page.check_suggest_not_visible()
