import pytest

from config_reader import ConfigReader
from pages.result_page import ResultPage
from pages.home_page import HomePage

config = ConfigReader()


@pytest.mark.parametrize("game_name", ["Fallout", "The Witcher"])
def test_filter_games(driver, game_name):
    main_page = HomePage(driver, timeout=config.WAIT_DEFAULT)
    main_page.open_page(config.base_steam)
    res_page = ResultPage(driver, timeout=config.WAIT_DEFAULT)

    main_page.open_page(config.base_steam)

    assert main_page.open_page(config.base_steam), "Главная страница еще не загрузилась"

    main_page.input_game_name(game_name)
    main_page.search_game()

    assert res_page.wait_success_open_page(), "Страница с результатами не открылась"

    res_page.filter_button()
    res_page.reduce_the_price()
