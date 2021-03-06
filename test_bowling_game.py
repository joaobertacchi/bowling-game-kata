import unittest

from game import Game


class TestBowlingGame(unittest.TestCase):

    def setUp(self):
        self.game = Game()

    def roll_many(self, pins, times):
        for i in range(times):
            self.game.roll(pins)

    def roll_spare(self):
        self.game.roll(5)
        self.game.roll(5)

    def roll_strike(self):
        self.game.roll(10)

    def test_gutter_game(self):
        self.roll_many(pins=0, times=20)

        assert self.game.score == 0

    def test_all_ones(self):
        self.roll_many(pins=1, times=20)

        assert self.game.score == 20

    def test_one_spare(self):
        self.roll_spare()
        self.game.roll(3)
        self.roll_many(pins=0, times=17)

        assert self.game.score == 16

    def test_one_strike(self):
        self.roll_strike()
        self.game.roll(3)
        self.game.roll(4)
        self.roll_many(pins=0, times=16)

        assert self.game.score == 24

    def test_perfect_game(self):
        self.roll_many(pins=10, times=12)

        assert self.game.score == 300

