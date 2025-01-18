import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import *
from circleshape import CircleShape
from bullet import Shot


def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    updatable_group = pygame.sprite.Group()
    drawable_group = pygame.sprite.Group()
    asteroid_group = pygame.sprite.Group()
    shot_group = pygame.sprite.Group()

    Player.containers = (updatable_group, drawable_group)
    player = Player(x=SCREEN_WIDTH / 2, y=SCREEN_HEIGHT / 2)
    Asteroid.containers = (asteroid_group, updatable_group, drawable_group)
    AsteroidField.containers = updatable_group
    field = AsteroidField()
    Shot.containers = (shot_group, updatable_group, drawable_group)

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
        for member in asteroid_group:
            if player.check_for_collisions(member):
                sys.exit("Game over!")
            for shot in shot_group:
                if shot.check_for_collisions(member):
                    shot.kill()
                    member.split()
        for member in drawable_group:
            member.draw(screen)
        # refreshes the display
        pygame.display.flip()

        # limit fps to 60
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
