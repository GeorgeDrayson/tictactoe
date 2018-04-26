import pytest
from turn_operator import Turn_Operator

class Player(object):
    def __init__(self):
        self.choices = [1,2,4]

def describe_turn_rotator():

    def test_starts_with_player1():
        player1 = Player()
        player2 = Player()
        operator = Turn_Operator(player1, player2)
        assert operator.turn() == player1

    def test_switches_to_player2():
        player1 = Player()
        player2 = Player()
        operator = Turn_Operator(player1, player2)
        operator.rotate_turns()
        assert operator.turn() == player2
