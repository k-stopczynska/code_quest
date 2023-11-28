import random
from falling_items.falling_items_factory import *
from board import Board
from player import Player
from stats.life import Life
from stats.level import Level
from stats.timer import Timer
from stats.points import Points
from decorators.sounds import Sounds
import pygame
import time
falling = FallingItemsFactory()

@Sounds("assets/sounds/soundtrack.mp3", loop=True)
def run():
    pygame.init()
    game_board = Board('Code Quest', (800, 600), 60)
    player = Player(800 - 725, 600 - 200, game_board, falling.python, falling.tick, falling.duck, falling.warning, falling.error, falling.bug)
    life = Life(player, game_board)
    level = Level(player, game_board)
    timer = Timer(player, game_board)
    points = Points(player, game_board)

    timer_seconds = 60
    start_time = time.time()

    # timer for making items fall
    falling.create_timer()

    while True:
        game_board.display_board()
        game_board.draw_background()
        life.draw(game_board)
        level.draw(game_board)
        points.draw(game_board)

        current_time = time.time()
        elapsed_time = current_time - start_time
        remaining_time = max(timer_seconds - int(elapsed_time), 0)
        timer.draw(game_board, timer=remaining_time)
        
        player.draw_player()
        player.move()

        falling.create_group()
        falling.set_fall_timer()
        falling.fall_and_respawn()

        player.check_falling_item_collision()
        game_board.update_display()


if __name__ == '__main__':
    run()
