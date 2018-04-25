import pytest
from player import Player

def describe_choose_method():

    def test_lets_you_choose_a_frame():
        player = Player()
        player.choose(1)
        assert 1 in player.choices

    def test_raises_error_if_outside_frame():
        player = Player()
        with pytest.raises(ValueError, match="That is not a valid frame"):
            player.choose(10)
