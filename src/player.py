class Player(object):

    def __init__(self):
        self.choices = []

    def choose(self, choice):
        self.choices.append(choice)
