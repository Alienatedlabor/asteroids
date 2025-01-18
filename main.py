import pygame
from constants import *
from player import Player


def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    updatable_group = pygame.sprite.Group()
    drawable_group = pygame.sprite.Group()

    Player.containers = (updatable_group, drawable_group)
    player = Player(x=SCREEN_WIDTH / 2, y=SCREEN_HEIGHT / 2)

    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # fills screen with black
        screen.fill((0, 0, 0))
        # iterates over all updateable and drawable objects and runs their respective update
        for member in updatable_group:
            member.update(dt)
        for member in drawable_group:
            member.draw(screen)
        # refreshes the display
        pygame.display.flip()

        # limit fps to 60
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
