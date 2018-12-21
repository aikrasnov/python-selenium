from src.pages.search import Search
from src.pages.main_page import MainPage
from src.wait.conditions import CONDITIONS
import pytest


@pytest.mark.parametrize("suggest_item", [{"text": "torrent", "position": "first"},
                                          {"text": "Мэил.ру", "position": "last"}])
@pytest.allure.testcase("http://test-tracker/suggest-3")
@pytest.allure.feature("SUGGEST-3: Поиск через саджест")
def test_suggest_3(driver, suggest_item):
    main = MainPage(driver)
    search = Search(driver)

    main.open()

    input_text = suggest_item["text"]
    item_position = suggest_item["position"]
    suggest_length = 10

    with pytest.allure.step(f"should type text '{input_text}'"):
        main.enter_query(input_text)
    with pytest.allure.step("suggest should be visible"):
        main.check_suggest_visible()
    with pytest.allure.step("should have more than one item in suggest"):
        main.check_suggest_item_count(CONDITIONS.equal, suggest_length)
    with pytest.allure.step(f"should get text from item {item_position}"):
        item_text = main.get_suggest_item_text(item_position)
    with pytest.allure.step(f"should click at '{item_position}' suggest item"):
        main.click_at_suggest_item(item_position)
    with pytest.allure.step(f"should open search page with '{item_text}' in input"):
        search.check_search_input_text(item_text)
