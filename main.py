import pygame
import sys
from constants import *
from player import *
from asteroid import *
from asteroidfield import *

def main():
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Asteroids")
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
    score = 0
    font = pygame.font.Font(None, 40)
    text = font.render("Score:", True, (135, 206, 235))

    background = pygame.image.load("space.jpg").convert()
    background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))
    
    explode = pygame.image.load("explode1.png").convert_alpha()
    explode = pygame.transform.scale(explode, (50, 50))

    while True: 
        screen.blit(background, (0, 0))
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
                    shoot.kill()
                    score += 2
                    text = font.render(f"Score: {score}", True, (135, 206, 235))
                    asteroid.split()
                    screen.blit(explode, asteroid.position)
                
        screen.blit(text, (SCREEN_WIDTH / 2 - 40, 10))
        for x in drawable:
            x.draw(screen)

        pygame.display.flip()
        time = clock.tick(60)
        dt = time / 1000

if __name__ == "__main__":
    main()
