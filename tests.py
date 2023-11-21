import unittest
import pygame
import numpy as np
from unittest.mock import patch, MagicMock
from board import Board
from player import Player


class TestBoard(unittest.TestCase):

    def setUp(self):
        pygame.init()

    def test_board_initialization(self):
        name = "TestBoard"
        res = (800, 600)
        frames = 60
        test_board = Board(name, res, frames)

        self.assertEqual(test_board.name, name)
        self.assertEqual(test_board.res, res)
        self.assertEqual(test_board.frames, frames)

    def test_display_board_initialization(self):
        name = "TestBoard"
        res = (800, 600)
        frames = 60
        test_board = Board(name, res, frames)
        test_board.display_board()

        self.assertEqual(pygame.display.get_caption()[0], "TestBoard")

    def test_update_display_board(self):
        name = "TestBoard"
        res = (800, 600)
        frames = 60
        test_board = Board(name, res, frames)
        test_result = test_board.update_display()
        self.assertEqual(test_result, 'Display updated')

    def test_draw_background(self):
        name = "TestBoard"
        res = (800, 600)
        frames = 60
        test_board = Board(name, res, frames)
        test_board.draw_background()
        board_content = pygame.surfarray.array3d(test_board.board)
        loaded_background = pygame.image.load("assets/background.jpg")
        loaded_background = pygame.transform.scale(loaded_background, res)
        background_content = pygame.surfarray.array3d(loaded_background)
        diff = np.abs(board_content - background_content)
        total_diff = np.sum(diff)
        allowable_diff = 0

        self.assertEqual(board_content.shape, background_content.shape)
        self.assertLessEqual(total_diff, allowable_diff)

    def test_quit_event_handling(self):
        name = "TestBoard"
        res = (800, 600)
        frames = 60
        test_board = Board(name, res, frames)

        with patch('pygame.event.get', return_value=[MagicMock(type=pygame.QUIT)]):
            with self.assertRaises(SystemExit):
                test_board.display_board()

    def tearDown(self):
        pygame.quit()


class TestPlayer(unittest.TestCase):
    def setUp(self):
        pygame.init()
        self.board = pygame.display.set_mode(
            (800, 600))
        self.test_board = Board("Test Board", (800, 600), 60)

    def test_player_initialization(self):
        player = Player(100, 100, self.test_board)

        self.assertEqual(player.rect.center, (100, 100))
        self.assertEqual(player.width, 100)
        self.assertEqual(player.height, 90)

    def test_draw_player(self):
        player = Player(100, 100, self.test_board)
        player.draw_player()
        player = pygame.surfarray.array3d(player.image)
        loaded_player = pygame.image.load("assets/player.png")
        loaded_player = pygame.transform.scale(loaded_player, (100,100))
        player_content = pygame.surfarray.array3d(loaded_player)
        diff = np.abs(player_content - player)
        total_diff = np.sum(diff)
        allowable_diff = 0

        self.assertLessEqual(total_diff, allowable_diff)

    def tearDown(self):
        pygame.quit()










