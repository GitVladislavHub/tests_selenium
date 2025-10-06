import time

import pytest
from pages.result_page import ResultPage
from pages.home_page import HomePage
from config_reader import get_config

config = get_config()


@pytest.mark.parametrize("game_name", ["Fallout", "The Witcher"])
def test_filter_games(driver, game_name):
    main_page = HomePage(driver, timeout=config.WAIT_DEFAULT)
    main_page.open(HomePage.URL)
    res_page = ResultPage(driver, timeout=config.WAIT_DEFAULT)

    main_page.check_page()

    assert main_page.visible_unique_element(HomePage.CAROUSEL_ITEMS), "Главная страница еще не загрузилась"

    main_page.input_game_name(game_name).click_search_button(game_name)

    assert res_page.success_open_page(), "Страница с результатами не открылась"

    res_page.filter_button()
    res_page.reduce_the_price()

    time.sleep(2)
