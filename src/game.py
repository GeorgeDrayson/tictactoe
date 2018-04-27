from player import Player
from turn_operator import Turn_Operator
from checker import Checker

class Game(object):

    def __init__(self, player1 = Player('X'), player2 = Player('O'), operator = Turn_Operator, Checker = Checker):
        self.checker = Checker()
        self.turn_operator =  Turn_Operator(player1, player2)

    def choose(self, choice):
        self.turn_operator.turn().choose(choice)
