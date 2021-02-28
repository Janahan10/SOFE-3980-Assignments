from unittest import TestCase

from __init__ import Snake

HEIGHT, WIDTH = 500, 700


class TestSnake(TestCase):
    def setUp(self):
        self.snake = Snake(WIDTH // 2, HEIGHT // 2)


class TestInit(TestSnake):
    def test_initial_position_x(self):
        self.assertEqual(self.snake.x, WIDTH // 2)

    def test_initial_position_y(self):
        self.assertEqual(self.snake.y, HEIGHT // 2)

    def test_initial_horizontal_velocity(self):
        self.assertEqual(self.snake.dx, 0)

    def test_initial_vertical_velocity(self):
        self.assertEqual(self.snake.dy, 0)


class TestMove(TestSnake):
    def test_move_left(self):
        self.snake.move('left')
        self.assertEqual(self.snake.dx, -10)

    def test_move_right(self):
        self.snake.move('right')
        self.assertEqual(self.snake.dx, 10)

    def test_move_up(self):
        self.snake.move('up')
        self.assertEqual(self.snake.dy, -10)

    def test_move_down(self):
        self.snake.move('down')
        self.assertEqual(self.snake.dy, 10)

