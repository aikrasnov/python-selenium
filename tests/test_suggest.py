from src.pages.go_mail_ru import GoMailRu
import pytest


@pytest.mark.parametrize('text', ['foobar', 'бесплатно', 'без смс'])
def test_suggest_chrome(chrome, text):
    page = GoMailRu(chrome)

    input_text = 'foobar'

    page.check_suggest_not_visible()
    page.enter_query(input_text)
    page.check_suggest_visible()
    page.check_suggest_text(input_text)
    page.clear_query()
    page.check_suggest_not_visible()
