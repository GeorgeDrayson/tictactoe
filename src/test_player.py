import pytest
from player import Player

def describe_choose_method():

    def test_lets_you_choose_a_frame():
        player = Player()
        player.choose(1)
        assert 1 in player.choices
