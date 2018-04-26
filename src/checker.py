class Checker(object):

    def win_check(self, player):
        for combo in self.combinations():
            return all(x in player.choices for x in combo)

    def combinations(self):
        return [[1,2,3], [4,5,6], [7,8,9], [1,4,7], [2,5,8],
        [3,6,9], [1,5,9], [3,5,7]]
