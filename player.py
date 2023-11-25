import pygame
from board import Board
from falling_items.points_falling_item import PythonItem, TickItem, RubberDuckItem
from falling_items.damage_falling_item import WarningItem, ErrorItem, BugItem
from typing import List
import datetime


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, board_instance: Board, python_instance: PythonItem, tick_instance: TickItem, duck_instance: RubberDuckItem, warning_instance: WarningItem, error_instance: ErrorItem, bug_instance: BugItem):        
        super().__init__()
        self.sprites_right = []
        self.sprites_right.append(pygame.image.load("assets/player_idle.png"))
        self.sprites_right.append(pygame.image.load("assets/player1.png"))
        self.sprites_right.append(pygame.image.load("assets/player2.png"))
        self.sprites_right.append(pygame.image.load("assets/player3.png"))
        self.sprites_right.append(pygame.image.load("assets/player4.png"))
        self.sprites_right.append(pygame.image.load("assets/player5.png"))
        self.sprites_right.append(pygame.image.load("assets/player6.png"))
        self.sprites_right.append(pygame.image.load("assets/player7.png"))
        self.sprites_right.append(pygame.image.load("assets/player8.png"))
        self.sprites_left = []
        self.sprites_left.append(pygame.image.load("assets/player_idle_left.png"))
        self.sprites_left.append(pygame.image.load("assets/player9.png"))
        self.sprites_left.append(pygame.image.load("assets/player10.png"))
        self.sprites_left.append(pygame.image.load("assets/player11.png"))
        self.sprites_left.append(pygame.image.load("assets/player12.png"))
        self.sprites_left.append(pygame.image.load("assets/player13.png"))
        self.sprites_left.append(pygame.image.load("assets/player14.png"))
        self.sprites_left.append(pygame.image.load("assets/player15.png"))
        self.sprites_left.append(pygame.image.load("assets/player16.png"))
        self.current_sprite = 0
        self.image = pygame.transform.scale(
            self.sprites_right[self.current_sprite], (100, 238))
        self.width = 100
        self.height = 90
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = (x, y)
        self.board_instance = board_instance
        self.life = 90
        self.points = 0
        self.damage = 0
        self.level = 1
        self.python_instance = python_instance
        self.tick_instance = tick_instance
        self.duck_instance = duck_instance
        self.warning_instance = warning_instance
        self.error_instance = error_instance
        self.bug_instance = bug_instance
        
        
    def draw_player(self):
        self.board_instance.board.blit(self.image, (self.rect.x,
                                                    self.rect.y - 10))

    def constrain_move_within_board(self, dx, dy):
        if self.rect.left + dx < 0:
            dx = -self.rect.left
        if self.rect.right + dx > self.board_instance.res[0]:
            dx = self.board_instance.res[0] - self.rect.right
        return dx, dy
    

    def animate(self, direction):
        self.current_sprite += 1
        if self.current_sprite >= 8:
            self.current_sprite = 0
        if direction == 'right':
            self.image = self.sprites_right[self.current_sprite]
            self.image = pygame.transform.scale(self.sprites_right[self.current_sprite],
                                            (100, 238))
        else:
            self.image = self.sprites_left[self.current_sprite]
            self.image = pygame.transform.scale(self.sprites_left[self.current_sprite],
                                            (100, 238))


    def move(self):
        # variable to reset for delta x and delta y
        dx = 0
        dy = 0
        key = pygame.key.get_pressed()
        if key[pygame.K_a] or key[pygame.K_LEFT]:
            dx = -10
            self.animate('left')
        if key[pygame.K_d] or key[pygame.K_RIGHT]:
            dx = 10
            self.animate('right')
        dx, dy = self.constrain_move_within_board(dx, dy)    

        self.rect.x += dx
        self.rect.y += dy
        
    
    def check_falling_item_collision(self):
        if self.rect.colliderect(self.python_instance.rect):
            print("You have hit the Python")
            self.points += self.python_instance.points
            self.damage += self.python_instance.damage
            self.python_instance.rect.topleft = (-100, -100)
            print(f"Player Points: {self.points}, Player Damage: {self.damage}")

        elif self.rect.colliderect(self.tick_instance.rect):
            print("You have hit the tick")
            self.points += self.tick_instance.points
            self.damage += self.tick_instance.damage
            self.tick_instance.rect.topleft = (-100, -100)
            print(f"Player Points: {self.points}, Player Damage: {self.damage}")
        
        elif self.rect.colliderect(self.duck_instance.rect):
            print("You have hit the Duck")
            self.points += self.duck_instance.points
            self.damage += self.duck_instance.damage
            self.duck_instance.rect.topleft = (-100, -100)
            print(f"Player Points: {self.points}, Player Damage: {self.damage}")
            
        elif self.rect.colliderect(self.warning_instance.rect):
            print("You have hit the Warning")
            self.points += self.warning_instance.points
            self.damage += self.warning_instance.damage
            self.warning_instance.rect.topleft = (-100, -100)
            print(f"Player Points: {self.points}, Player Damage: {self.damage}")
            
        elif self.rect.colliderect(self.error_instance.rect):
            print("You have hit the Error")
            self.points += self.error_instance.points
            self.damage += self.error_instance.damage
            self.error_instance.rect.topleft = (-100, -100)
            print(f"Player Points: {self.points}, Player Damage: {self.damage}")
            
        elif self.rect.colliderect(self.bug_instance.rect):
            print("You have hit the Bug")
            self.points += self.bug_instance.points
            self.damage += self.bug_instance.damage
            self.bug_instance.rect.topleft = (-100, -100)
            print(f"Player Points: {self.points}, Player Damage: {self.damage}")
