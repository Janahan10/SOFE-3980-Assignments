from unittest import TestCase

from __init__ import Obstacle


class TestObstacle(TestCase):
    def setUp(self):
        self.obstacle = Obstacle()


class TestInit(TestObstacle):
    def test_initialize_list(self):
        self.assertEqual(self.obstacle.list_obs, [])



