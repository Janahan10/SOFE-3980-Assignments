from unittest import TestCase

from __init__ import Snack

HEIGHT, WIDTH = 500, 700
SAFE_HEIGHT_MIN, SAFE_WIDTH_MIN = 45, 45
SAFE_HEIGHT_MAX, SAFE_WIDTH_MAX = HEIGHT - SAFE_HEIGHT_MIN, WIDTH - SAFE_WIDTH_MIN


class TestSnack(TestCase):
    def setUp(self):
        self.snack = Snack()


class TestInit(TestSnack):
    def test_no_position(self):
        self.assertEqual(self.snack.pos, ())


