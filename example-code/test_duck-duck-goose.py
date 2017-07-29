import pytest
import mock

from duck_duck_goose import *

"""
Pytest's test discovery is nifty.  It looks for anything in this
directory with the word 'test' in front of it.

All you have to worry about is making the tests.
"""
def test_test_discovery():
    working = True
    assert working == True

"""
Alternatively, you can intentionally skip tests by putting a character
before the word test or omit it altogether.
"""
def _test_this_will_not_be_discovered():
    assert True == False

"""
You can create test classes to group unit tests together
"""
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