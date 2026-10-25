from player import Player
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, PLAYER_RADIUS 
from logger import log_state
import pygame  

updatable = pygame.sprite.Group()
drawable = pygame.sprite.Group()

Player.containers = (updatable, drawable)

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0.0
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    player = Player(x, y, PLAYER_RADIUS )
    print("Updatable:", len(updatable))
    print("Drawable:", len(drawable))
   
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill("black")
        updatable.update(dt)
        for sprite in drawable:
            sprite.draw(screen)

        pygame.display.flip()
        dt = clock.tick(60) / 1000
        
   


if __name__ == "__main__":
    main()
