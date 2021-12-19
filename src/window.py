import pygame
from pathlib import PurePath
from .constants import (
    TITLE, ICON_PATH,
    SETTING_WIDTH, SETTING_HEIGHT,
    LIST_WIDTH, LIST_HEIGHT, LIST_MIN_HEIGHT,
    BACKGROUND_COLOR, LIST_COLORS, LIST_COLOR_ONE, LIST_COLOR_TWO,
    BLACK
)
pygame.init()


class Window:
    def __init__(self, width, height, algo_type, algo_name, lst, ascending=True):
        self.width = width                                                  # width
        self.height = height                                                # height

        self.screen = pygame.display.set_mode((width, height))              # screen
        pygame.display.set_caption(TITLE)                                   # title
        pygame.display.set_icon(pygame.image.load(PurePath(*ICON_PATH)))    # icon

        self.algo_type = algo_type
        self.algo_name = algo_name
        self.ascending = ascending

        self.set_setting()
        self.set_list(lst)

    def set_setting(self):
        self.setting = pygame.Surface((SETTING_WIDTH, SETTING_HEIGHT))
        self.draw_setting()

    def draw_setting(self):
        self.setting.fill(BACKGROUND_COLOR)
        font = pygame.font.SysFont("comicsans", self.setting.get_height()//5)
        text = font.render(self.algo_name, 1, BLACK)
        self.setting.blit(text, (5, 5))


    def set_list(self, lst):
        self.list = lst
        self.list_surface = pygame.Surface((LIST_WIDTH, LIST_HEIGHT))

        self.n = len(lst)
        self.min_value = min(lst)
        self.max_value = max(lst)

        self.list_item_width = LIST_WIDTH / self.n
        self.list_item_heigth = (LIST_HEIGHT - LIST_MIN_HEIGHT) / (self.max_value - self.min_value)
        self.draw_list_surface()

    def change_list(self, change, item_one, item_two):
        if change:
            self.list[item_one], self.list[item_two] = self.list[item_two], self.list[item_one]
            self.draw_list_surface(color_two_indexes=[item_one, item_two])
        else:
            self.draw_list_surface(color_one_indexes=[item_one])

    def draw_list_surface(self, color_one_indexes=[], color_two_indexes=[]):
        self.list_surface.fill(BACKGROUND_COLOR)
        for i, value in enumerate(self.list):
            x = self.list_item_width * i
            y = (self.max_value - value) * self.list_item_heigth
            width =  self.list_item_width
            height = self.list_item_heigth * value + LIST_MIN_HEIGHT

            if i in color_one_indexes:
                color = LIST_COLOR_ONE
            elif i in color_two_indexes:
                color = LIST_COLOR_TWO
            else:
                color = LIST_COLORS[i % len(LIST_COLORS)]
            pygame.draw.rect(self.list_surface, color, (x, y, width, height))
