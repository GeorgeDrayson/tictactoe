class Checker(object):

    def win_check(self, player):
        for combo in self.combinations():
            return all(x in player.choices for x in combo)

    def combinations(self):
        return [[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7],
        [2,5,8], [0,4,8], [2,4,6]]
