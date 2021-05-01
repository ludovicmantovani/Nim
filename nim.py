# import the pygame module, so you can use it
import pygame

# set resolution
WIDTH = 960
HEIGHT = 720
RESOLUTION = (WIDTH, HEIGHT)

# set colors
DARK = (43, 43, 43)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

DEFAULT_SCREEN_COLOR = DARK


class Match(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.smoothscale(
            pygame.transform.rotate(
                pygame.image.load("img/match640x640.png"),
                45.0),
            (90, 90))
        self.surf = pygame.Surface((90, 90))

    def draw(self, surface, position):
        surface.blit(
            self.image,
            self.surf.get_rect(
                center=position)
        )


def get_coord(nbr_element, elem_size, origin_pos):
    ret = {}
    middle = nbr_element / 2
    for index in range(nbr_element):
        index_delta = abs(middle - index)
        pos_delta = elem_size * index_delta
        if index < middle:
            pos_delta = pos_delta * -1
        else:
            pos_delta = pos_delta * 1
        glob_pos = pos_delta + + (elem_size / 2) + origin_pos
        ret[index] = glob_pos
    return ret


def draw_match_board(match_board, screen):
    lines_nbr = len(match_board)
    height_val = get_coord(lines_nbr, 100, HEIGHT / 2)
    for index, row in enumerate(match_board):
        width_val = get_coord(row, 22.5, WIDTH / 2)
        for k, val in width_val.items():
            m = Match()
            m.draw(screen, (val, height_val[index]))


def main():
    # print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    # initialize the pygame module
    pygame.init()
    # load and set the logo
    logo = pygame.image.load("img/logo32x32.png")
    pygame.display.set_icon(logo)
    pygame.display.set_caption("Nim program")

    # create a surface on screen that has the size of RESOLUTION and basic SCREEN_COLOR
    screen = pygame.display.set_mode(RESOLUTION, pygame.NOFRAME | pygame.SCALED)
    pygame.Surface.fill(screen, DEFAULT_SCREEN_COLOR)

    # define a variable to control the main loop
    running = True

    match_board = [
        1,
        3,
        7,
        15,
        15 + 15 + 1
    ]

    draw_match_board(match_board, screen)

    pygame.display.update()

    # main loop
    while running:
        # event handling, gets all event from the event queue
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_ESCAPE or event.key == pygame.key.key_code("escape"):
                    running = False
                elif event.key == pygame.K_SPACE or event.key == pygame.key.key_code("space"):
                    truncated = False
                    for index, nb in enumerate(match_board):
                        if not truncated:
                            if nb > 0:
                                match_board[index] = nb - 1
                                truncated = True
                    pygame.Surface.fill(screen, DEFAULT_SCREEN_COLOR)
                    draw_match_board(match_board, screen)
                    pygame.display.update()


# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__ == "__main__":
    # call the main function
    main()
