import pygame
import sys
from menus.menu import Menu
from db.history import get_history_data
from board import Board
from models.components.button import Button
from utils import assets_library

pygame.font.init()
font = pygame.font.Font(assets_library['fonts']['kiddy_play'], 30)


class HistoryMenu(Menu):
    """
    Represents the history menu for users to see their stats.

    Attributes:
        history (bool): Flag indicating whether the history menu is active.
        background_image (pygame.Surface): The background image for the history menu.
        column_names (list): A list of column names for displaying history data.
    """
    
    def __init__(self, board_instance: Board):
        """
        Initialise the HistoryMenu.

        Args:
            board_instance (Board): The game board instance.
        """
        super().__init__(board_instance)
        self.history = True
        self.background_image = pygame.image.load(assets_library['backgrounds']['registration_page'])
        self.column_names = ["Username", "Points", "Life", "Level"]

    def get_play_again(self):
        """
        Get the play_again status.

        Returns:
            bool: The play_again status.
        """
        return self.play_again

    def play_again_handler(self):
        """
        Handle the play again action.

        Set the play_again flag to True.
        """
        self.play_again = True
        
    def exit_game_handler(self):
        """
        Handle the exit game action.

        Quit the pygame application and exit the system.
        """
        pygame.quit()
        sys.exit()
        
    def draw(self):
        """
        Draw the history menu on the board.

        Display the background image, title, column names, data and button.
        """
        player_data = get_history_data()
        background_image = pygame.image.load(assets_library['backgrounds']['registration_page'])
        background_image = pygame.transform.scale(background_image, (800, 600))
        self.board_instance.board.blit(background_image, (0, 0))

        title_text = font.render("HISTORY", True, (255, 255, 255))
        self.board_instance.board.blit(title_text, (350, 180))

        column_x = 150
        column_y = 230
        for col_name in self.column_names:
            col_text = font.render(col_name, True, (255, 255, 255))
            self.board_instance.board.blit(col_text, (column_x, column_y))
            column_x += 150

        data_y = 270
        for row in player_data:
            data_x = 150
            for value in row:
                value_text = font.render(str(value), True, (255, 255, 255))
                self.board_instance.board.blit(value_text, (data_x, data_y))
                data_x += 150
            data_y += 30

        play_button = Button(200, 550, 150, 40, self.board_instance, buttonText='Play', onclickFunction=self.play_again_handler, onePress=False)
        exit_button = Button(450, 550, 150, 40, self.board_instance, buttonText='Exit', onclickFunction=self.exit_game_handler, onePress=False)
        back_button = Button(20, 10, 200, 40, self.board_instance, 'BACK TO MENU')
        play_button.process()
        exit_button.process()
        back_button.process()

        pygame.display.update()
        self.history = False
