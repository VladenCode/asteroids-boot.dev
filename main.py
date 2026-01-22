import pygame
from constants import *
from logger import log_state
from player import Player

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    clock = pygame.time.Clock()
    fps = 60
    dt = 0

    player = Player((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))

    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")

    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill("black")
        player.draw(screen)
        pygame.display.flip()

        dt = clock.tick(fps)/1000


if __name__ == "__main__":
    main()
