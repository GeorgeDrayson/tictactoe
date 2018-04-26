class Turn_Operator(object):

    def __init__(self, player1, player2):
        self.players = [player1, player2]

    def turn(self):
        return self.players[0]

    def rotate_turns(self):
        self.players.reverse()
