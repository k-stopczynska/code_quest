import pygame
from board import Board
from utils import assets_library

pygame.font.init()
font = pygame.font.Font(assets_library['fonts']['kiddy_play'], 30)


class TextDrawer:
    def __init__(self, board_instance: Board):
        self.board_instance = board_instance

    # Draw text in the center of the game board.
    def draw_text(self, text, text_color, x, y, font):
        img = font.render(text, True, text_color)
        location = img.get_rect()

        # Calculate the starting position for centering the text
        start_text = int(self.board_instance.res[0] / 2 - location.center[0])
        self.board_instance.board.blit(img, (start_text, y))