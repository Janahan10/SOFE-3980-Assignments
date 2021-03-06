import timeit

import pygame
import random

pygame.init()

HEIGHT, WIDTH = 500, 700
SAFE_HEIGHT_MIN, SAFE_WIDTH_MIN = 45, 45
SAFE_HEIGHT_MAX, SAFE_WIDTH_MAX = HEIGHT - SAFE_HEIGHT_MIN, WIDTH - SAFE_WIDTH_MIN
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
LIME_GREEN = (50, 205, 50)
RED = (255, 0, 0)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.font.init()
regular_font = pygame.font.SysFont("YuseiMagic-Regular.ttf", 25)
big_font = pygame.font.SysFont("YuseiMagic-Regular.ttf", 45)

# list for counting number of calls
num_calls = [0] * 5
# list to keep track of time elasped per function
time_list = [0] * 5
# name of each function
names = ['generate_snack', 'detect_touch', 'update_screen', 'end_game', 'generate_obstacle']
headings = ['Method Name', 'Number of Calls', 'Time Per Call']


class Snack(object):
    def __init__(self, pos=None):
        if not pos:
            self.pos = ()
        else:
            self.pos = pos

    def generate_snack(self, player_pos):
        num_calls[0] += 1
        t_start = timeit.default_timer()
        while True:
            snack_x, snack_y = random.randrange(SAFE_WIDTH_MIN, SAFE_WIDTH_MAX), \
                               random.randrange(SAFE_HEIGHT_MIN, SAFE_HEIGHT_MAX)

            if snack_x == player_pos[0] and snack_y == player_pos[1]:
                continue
            else:
                break

        self.pos = (snack_x, snack_y)

        t_end = timeit.default_timer()
        time_list[0] = t_end - t_start

    def draw(self):
        pygame.draw.rect(screen, LIME_GREEN, (self.pos[0], self.pos[1], 40, 40))


class Obstacle(object):
    def __init__(self):
        self.list_obs = []

    def detect_touch(self, player_pos):

        num_calls[1] += 1
        t_start = timeit.default_timer()

        for obs in self.list_obs:
            if obs[0] <= player_pos[0] <= obs[0] + 40 and obs[1] <= player_pos[1] <= obs[1] + 40:
                return True

        return False

        t_end = timeit.default_timer()
        time_list[1] = t_end - t_start

    def generate_obstacle(self, player_pos):

        num_calls[4] += 1
        t_start = timeit.default_timer()

        while True:
            obs_x, obs_y = random.randrange(SAFE_WIDTH_MIN, SAFE_WIDTH_MAX), \
                           random.randrange(SAFE_HEIGHT_MIN, SAFE_HEIGHT_MAX)

            if obs_x == player_pos[0] and obs_y == player_pos[1]:
                continue
            else:
                break

        if len(self.list_obs) == 5:
            self.list_obs.pop()
        self.list_obs.append((obs_x, obs_y))

        t_end = timeit.default_timer()
        time_list[4] = t_end - t_start

    def draw(self):
        for obs in self.list_obs:
            pygame.draw.rect(screen, RED, (obs[0], obs[1], 40, 40))


class Snake(object):
    def __init__(self, x=None, y=None):
        self.x = x
        self.y = y
        self.dx = 0
        self.dy = 0

    def move(self, direction):
        if direction == 'left':
            self._move_left()
        elif direction == 'right':
            self._move_right()
        elif direction == 'up':
            self._move_up()
        elif direction == 'down':
            self._move_down()

    def _move_left(self):
        self.dx = -10
        self.dy = 0

        self.x += self.dx
        if self.x < 0:
            self.x = WIDTH
        if self.x > WIDTH:
            self.x = 0

    def _move_right(self):
        self.dx = 10
        self.dy = 0

        self.x += self.dx
        if self.x < 0:
            self.x = WIDTH
        if self.x > WIDTH:
            self.x = 0

    def _move_up(self):
        self.dx = 0
        self.dy = -10

        self.y += self.dy
        if self.y < SAFE_HEIGHT_MIN:
            self.y = HEIGHT
        if self.y > HEIGHT:
            self.y = SAFE_HEIGHT_MIN

    def _move_down(self):
        self.dx = 0
        self.dy = 10

        self.y += self.dy
        if self.y < SAFE_HEIGHT_MIN:
            self.y = HEIGHT
        if self.y > HEIGHT:
            self.y = SAFE_HEIGHT_MIN

    def draw(self):
        pygame.draw.rect(screen, WHITE, (self.x, self.y, 20, 20))


def update_screen(snake, snack, obstacle, score):
    num_calls[2] += 1
    t_start = timeit.default_timer()

    screen.fill(BLACK)
    snake.draw()
    snack.draw()
    obstacle.draw()
    update_score(score)
    pygame.display.update()

    t_end = timeit.default_timer()
    time_list[2] = t_end - t_start


def end_game(score):
    num_calls[3] += 1
    t_start = timeit.default_timer()

    screen.fill(BLACK)
    score_text = big_font.render("FINAL SCORE: " + str(score), True, WHITE)
    game_over_text = big_font.render("GAME OVER!!!!", True, RED)
    screen.blit(game_over_text, (235, 200))
    screen.blit(score_text, (230, 300))
    pygame.display.update()
    pygame.time.delay(2500)

    t_end = timeit.default_timer()
    time_list[3] = t_end - t_start

    pygame.quit()
    #quit()


def increment_score(score):
    return score + 1


def update_score(score):
    text = regular_font.render("SCORE: " + str(score), True, WHITE)
    score_text = big_font.render("SCORE: " + str(score), True, WHITE)
    screen.blit(text, (30, 30))


def game_loop(snake):
    is_game_over = False
    score = 0
    clock = pygame.time.Clock()

    snack = Snack()
    snack.generate_snack((snake.x, snake.y))

    obstacle = Obstacle()

    for _ in range(5):
        obstacle.generate_obstacle((snake.x, snake.y))

    while not is_game_over:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                is_game_over = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    snake.move('left')
                elif event.key == pygame.K_RIGHT:
                    snake.move('right')
                elif event.key == pygame.K_UP:
                    snake.move('up')
                elif event.key == pygame.K_DOWN:
                    snake.move('down')

        if snake.dx > 0:
            snake.move('right')
        if snake.dx < 0:
            snake.move('left')
        if snake.dy < 0:
            snake.move('up')
        if snake.dy > 0:
            snake.move('down')

        if snack.pos[0] <= snake.x <= snack.pos[0] + 40 and snack.pos[1] <= snake.y <= snack.pos[1] + 40:
            score = increment_score(score)
            snack.generate_snack((snake.x, snake.y))
            obstacle.generate_obstacle((snake.x, snake.y))

        if obstacle.detect_touch((snake.x, snake.y)):
            game_over = True
            break

        update_screen(snake, snack, obstacle, score)
        clock.tick(30)

    end_game(score)


def main():
    pygame.init()
    player = Snake(WIDTH // 2, HEIGHT // 2)
    game_loop(player)


if __name__ == "__main__":
    main()
    print('\n' + '\t\t\t'.join(headings))

    # first method
    print(str(names[0] + '\t\t\t' + str(num_calls[0]) + '\t\t\t\t\t\t' + str(time_list[0])))
    print(str(names[1] + '\t\t\t' + str(num_calls[1]) + '\t\t\t\t\t\t' + str(time_list[1])))
    print(str(names[2] + '\t\t\t' + str(num_calls[2]) + '\t\t\t\t\t\t' + str(time_list[2])))
    print(str(names[3] + '\t\t\t\t' + str(num_calls[3]) + '\t\t\t\t\t\t' + str(time_list[3])))
    print(str(names[4] + '\t\t' + str(num_calls[4]) + '\t\t\t\t\t\t' + str(time_list[4])))
