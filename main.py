import pygame
import sys
from constants import *
from player import *
from asteroid import *
from asteroidfield import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shoots = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    asteroid_feild = AsteroidField()
    
    Player.containers = (updatable, drawable)
    
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    
    Shot.containers = (shoots, updatable, drawable)

    while True: 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        updatable.update(dt)    

        for asteroid in asteroids:
            if asteroid.hasCollision(player):
                print("Game Over!")
                sys.exit()
            for shoot in shoots:
                if shoot.hasCollision(asteroid):
                    asteroid.split()
                    shoot.kill()
                
        screen.fill("black")
        for x in drawable:
            x.draw(screen)

        pygame.display.flip()
        time = clock.tick(60)
        dt = time / 1000

if __name__ == "__main__":
    main()
