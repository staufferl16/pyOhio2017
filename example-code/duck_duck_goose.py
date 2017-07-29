import random


class DuckDuckGoose:

    def __init__(self, number_of_players=5, game_odds=14):
        self.players=number_of_players
        self.current_player=1
        self.odds=game_odds
        self.duck_or_goose = 'Duck'
        self.is_over=False

    def go_to_next_player(self):
        if self.current_player+1 > self.players:
            self.current_player = 1
        else:
            self.current_player+=1

    def create_random_number(self):
        return random.randint(0, self.odds)

    def decide_if_goose(self, game_number):
        if game_number == 1:
            return True
        else:
            return False

    def play_game(self):
        random_number = self.create_random_number()
        is_goose = self.decide_if_goose(random_number)
        if not is_goose:
            print('Player {0}:  {1}'.format(self.current_player, self.duck_or_goose))
            self.go_to_next_player()
            self.play_game()
        else:
            self.duck_or_goose = 'Goose!!!'
            print('Player {0} is {1}'.format(self.current_player, self.duck_or_goose))
            self.is_over=True

def check_for_valid_odds(odds):
    if 1 < odds > 15:
        raise ValueError('Number must be between 1 and 15')

def play_duck_duck_goose():

    players = input('How many people are playing?    ')
    odds = input('Pick a number between 1 and 15:    ')

    check_for_valid_odds(odds)

    current_game = DuckDuckGoose(players, odds)

    while current_game.is_over != True:
        current_game.play_game()

if __name__ == "__main__":
    play_duck_duck_goose()
