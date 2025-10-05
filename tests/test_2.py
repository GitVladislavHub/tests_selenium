import pytest
from pages.result_page import ResultPage
from pages.home_page import HomePage


@pytest.mark.parametrize("game_name", ["Fallout", "The Witcher"])
def test_filter_games(lang, driver, game_name):
    main_page = HomePage(driver)
    res_page = ResultPage(driver)

    main_page.open().visible_el_home_page_steam()

    assert main_page.visible_el_home_page_steam(), "Главная страница еще не загрузилась"

    main_page.input_game_name(game_name).click_button(game_name)

    assert res_page.success_open_page(), "Страница с результатами не открылась"

    res_page.filter_button()
    res_page.decreasing_price()
