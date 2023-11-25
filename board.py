import pygame
import sys

background_image = pygame.image.load("assets/background.jpg")


class Board:
    def __init__(self, name, res, frames):
        self.name = name
        self.res = res
        self.frames = frames
        self.image = pygame.transform.scale(background_image, (self.res))
        self.board = pygame.display.set_mode(self.res)
        self.board_surface = pygame.Surface((self.res[0], self.res[1]))
        self.pause = False
    
    def display_board(self):
        pygame.display.set_caption(self.name)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.pause = not self.pause


    def update_display(self):
        fps = pygame.time.Clock()
        pygame.display.update()
        fps.tick(self.frames)

    def draw_background(self):
        self.board.blit(self.image, (0, 0))
