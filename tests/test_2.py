import pytest

from config_reader import ConfigReader
from pages.result_page import ResultPage
from pages.home_page import HomePage

config = ConfigReader()


@pytest.mark.parametrize(("game_name", "limit_prices"), [("Fallout", 20), ("The Witcher", 10)])
def test_filter_games(driver, game_name, limit_prices):
    main_page = HomePage(driver, timeout=config.timeouts["wait_default"])
    res_page = ResultPage(driver, timeout=config.timeouts["wait_default"])

    main_page.driver.get(config.base_urls["steam"])

    assert main_page.is_success_open_page(), 'Страница не открылась'

    main_page.input_game_name(game_name)
    main_page.search_game()

    assert res_page.wait_success_open_page(), "Страница с результатами не открылась"

    res_page.filter_button()
    res_page.reduce_the_price()

    res_page.wait_until_results_updated()
    res_page.games_filter(limit_prices)

    #assert