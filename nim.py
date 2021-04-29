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
            pygame.image.load("img/match640x640.png"), (64, 64))
        self.surf = pygame.Surface((64, 64))

    def draw(self, surface, position):
        surface.blit(
            self.image,
            self.surf.get_rect(
                center=position)
        )


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

    # Draw elements
    pygame.draw.line(screen, RED, (0, HEIGHT / 2), (WIDTH, HEIGHT / 2))
    pygame.draw.line(screen, RED, (WIDTH / 2, 0), (WIDTH / 2, HEIGHT))
    m1 = Match()
    m1.draw(screen, (WIDTH / 2, HEIGHT / 2))
    pygame.display.update()

    # define a variable to control the main loop
    running = True

    # main loop
    while running:
        # event handling, gets all event from the event queue
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False

            keys = pygame.key.get_pressed()

            if keys[pygame.K_ESCAPE] or keys[pygame.key.key_code("escape")]:
                running = False


# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__ == "__main__":
    # call the main function
    main()
