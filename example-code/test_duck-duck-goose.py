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


"""It will tell you EXACTLY where things went wrong, making debugging a cinch"""
def _test_showing_error():
    assert 'This string is cool' == 'This string is rad'

def _test_really_big_string_error():
    example_string_1 = '0'*1000 + 'a' + '1'*1000
    example_string_2 = '0'*1000 + 'b' + '1'*1000

    assert example_string_1 == example_string_2

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

"""
Fixtures can simplify your testing life.
"""
@pytest.fixture
def game():
    return DuckDuckGoose()

def test_game_defaults():
    new_game = game()
    assert new_game.players == 5
    assert new_game.odds == 14

"""
You can use pytest fixtures to create a collection of test parameters.
Great for dummy checking functions that have edge-cases or perform
non-trivial data manipulation
"""
@pytest.mark.parametrize('test_input,expected', [
    (3, False),
    (15, False),
    (10, False),
    (1, True)
])
def test_decide_if_goose(test_input, expected):
    new_game = DuckDuckGoose()
    assert new_game.decide_if_goose(test_input) == expected
