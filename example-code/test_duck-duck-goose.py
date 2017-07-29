import pytest
import mock

from duck_duck_goose import *

#You can create test classes to group unit tests together
class TestDuckDuckGoose:

    # Unit testing is such a *~breeze~* with mocks!
    def test_init(self):
        fake_number_of_players=mock.Mock()
        fake_odds=mock.Mock()

        my_game = DuckDuckGoose(fake_number_of_players, fake_odds)

        assert my_game.players == fake_number_of_players
        assert my_game.odds == fake_odds

    # You can test to make sure things failed as expected
    def test_bad_odds(self):
        bad_odds = 365

        with pytest.raises(ValueError) as bad:
            check_for_valid_odds(bad_odds)

        assert bad.type == ValueError

    # You can use fixtures to