import pytest
from checker import Checker

class Player(object):
    def __init__(self):
        self.choices = [1,2,4]

def describe_win_check_that_will_fail():

    def test_returns_false_if_no_winning_combos():
        checker = Checker()
        player = Player()
        assert checker.win_check(player) == False

def describe_win_check_that_will_pass():

    def test_returns_false_if_no_winning_combos():
        checker = Checker()
        player = Player()
        player.choices = [1,2,3]
        assert checker.win_check(player) == True
