import pygame
from constants import (
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
    ASTEROID_MIN_RADIUS,
    ASTEROID_MAX_RADIUS,
    ASTEROID_KINDS,
    ASTEROID_SPAWN_RATE,
)
from player import Player

player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0  # delta time
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill((0, 0, 0))
        player.draw(screen)
        player.update(dt)

        pygame.display.flip()
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
