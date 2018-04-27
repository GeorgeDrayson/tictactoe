class Player(object):

    def __init__(self, symbol):
        self.choices = []
        self.symbol = symbol

    def choose(self, choice):
        if choice > 9: raise ValueError('That is not a valid frame')
        self.choices.append(choice)
