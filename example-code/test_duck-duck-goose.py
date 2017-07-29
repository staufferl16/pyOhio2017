import sys
import os

from duck_duck_goose import DuckDuckGoose

class TestDuckDuckGoose:

    def test_init(self):
        fake_number_of_players=35
        fake_odds=12

        my_game = DuckDuckGoose(fake_number_of_players, fake_odds)

        assert my_game.players == fake_number_of_players
        assert my_game.odds == fake_odds