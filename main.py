import pygame
from src.window import Window
from src.list import generate_random_list
from src.constants import (
    WIDTH, HEIGHT,
    FPS, BACKGROUND_COLOR,
    ALGORITHM_TYPE, ALGORITHM_NAME,
    NUMBER_OF_ITEMS, MIN_VALUE, MAX_VALUE,
    LIST_POS_X, LIST_POS_Y
)


def draw_window(window):
    window.screen.fill(BACKGROUND_COLOR)

    window.screen.blit(window.list_surface, (LIST_POS_X, LIST_POS_Y))

    pygame.display.update()


def main():
    running = True
    clock = pygame.time.Clock()

    random_list = generate_random_list(NUMBER_OF_ITEMS, MIN_VALUE, MAX_VALUE)
    window = Window(WIDTH, HEIGHT, ALGORITHM_TYPE, ALGORITHM_NAME, random_list)

    while running:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break

        draw_window(window)

    pygame.quit()


if __name__ == "__main__":
    main()
