import pytest

from config_reader import ConfigReader
from pages.result_page import ResultPage
from pages.home_page import HomePage

config = ConfigReader()


@pytest.mark.parametrize("game_name", ["Fallout", "The Witcher"])
def test_filter_games(driver, game_name):
    main_page = HomePage(driver, timeout=config.WAIT_DEFAULT)
    main_page.open()
    res_page = ResultPage(driver, timeout=config.WAIT_DEFAULT)

    main_page.is_check_page()

    assert main_page.is_check_page(), "Главная страница еще не загрузилась"

    main_page.input_game_name(game_name).search_game(game_name)

    assert res_page.wait_success_open_page(), "Страница с результатами не открылась"

    res_page.filter_button()
    res_page.reduce_the_price()
