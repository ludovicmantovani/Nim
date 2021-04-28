# import the pygame module, so you can use it
import pygame

# set resolution
WIDTH = 960
HEIGHT = 720
RESOLUTION = (WIDTH, HEIGHT)

# set colors
WHITE_COLOR = (255, 255, 255)
SCREEN_COLOR = WHITE_COLOR


# define a main function
def main():
    #print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    # initialize the pygame module
    pygame.init()
    # load and set the logo
    logo = pygame.image.load("img/logo32x32.png")
    pygame.display.set_icon(logo)
    pygame.display.set_caption("Nim program")

    # create a surface on screen that has the size of RESOLUTION and basic SCREEN_COLOR
    screen = pygame.display.set_mode(RESOLUTION)
    pygame.Surface.fill(screen, SCREEN_COLOR)
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


# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__ == "__main__":
    # call the main function
    main()