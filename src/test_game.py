import pytest
from game import Game
from player import Player

from doubles import InstanceDouble, allow
from doubles import expect

class Turn_Operator(object):

    def __init__(self, player1, player2):
        self.players = [player1, player2]

    def turn(self):
        return self.players[0]

def describe_choose_method():

    def test_calls_choose_on_player():
        player1 = InstanceDouble('player.Player')
        player2 = InstanceDouble('player.Player')

        expect(player1).choose.exactly(1).time

        game = Game(player1, player2, Turn_Operator)
        game.choose(2)
