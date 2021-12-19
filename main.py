import pygame
from src.window import Window
from src.list import generate_random_list
from src.algorithms.sorting import bubble_sort
from src.constants import (
    WIDTH, HEIGHT,
    FPS, BACKGROUND_COLOR,
    ALGORITHM_TYPE, ALGORITHM_NAME,
    NUMBER_OF_ITEMS, MIN_VALUE, MAX_VALUE,
    LIST_POS_X, LIST_POS_Y
)


def set_algorithm(window):
    if window.algo_type == "sorting":
        if window.algo_name == "bubble_sort":
           return bubble_sort(window.list, window.ascending)


def draw_window(window):
    window.screen.fill(BACKGROUND_COLOR)

    window.screen.blit(window.list_surface, (LIST_POS_X, LIST_POS_Y))

    pygame.display.update()


def main():
    running = True
    clock = pygame.time.Clock()

    random_list = generate_random_list(NUMBER_OF_ITEMS, MIN_VALUE, MAX_VALUE)
    window = Window(WIDTH, HEIGHT, ALGORITHM_TYPE, ALGORITHM_NAME, random_list)

    solving = False
    algorithm = set_algorithm(window)

    while running:
        clock.tick(FPS)

        if solving:
            try:
                change, item_one, item_two = next(algorithm)
                window.change_list(change, item_one, item_two)
            except StopIteration:
                solving = False
                window.draw_list_surface()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    solving = True
                elif event.key == pygame.K_d:
                    window.ascending = False
                    algorithm = set_algorithm(window)
                elif event.key == pygame.K_q:
                    running = False
                    break

        draw_window(window)

    pygame.quit()


if __name__ == "__main__":
    main()
