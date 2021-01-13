#Made by Alexander Thomas
import pygame
import sys
import random
from pygame import mixer
pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((1500, 1024))
clock = pygame.time.Clock()

bg_surface = pygame.image.load('SpaceFlight - assets/space.jpg').convert()
bg_x_pos = 0

bg_surface2 = pygame.image.load('SpaceFlight - assets/space.jpg').convert()
bg2_x_pos = 1500

mixer.music.load('SpaceFlight - assets/spaceLofi (2).wav')
mixer.music.play(-1)

ship_surface = pygame.image.load('SpaceFlight - assets/Sarux03Propel (3).png').convert_alpha()
ship_x_pos = 100
ship_y_pos = 300
ship_movement = 5
ship_rect = ship_surface.get_rect(center=(ship_x_pos, ship_y_pos))

asteroid_surface = pygame.image.load('SpaceFlight - assets/asteroid.png').convert_alpha()
asteroid_x_pos = 1500
asteroid_y_pos = random.randint(30, 850)
asteroid_speed = 6
asteroid_rect = asteroid_surface.get_rect(center=(asteroid_x_pos, asteroid_y_pos))

font = pygame.font.Font(None, 74)
GOLD = (255, 198, 0)

score = 0
allySpawn = 1

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        ship_y_pos -= ship_movement
        ship_surface = pygame.image.load('SpaceFlight - assets/Sarux03Propel (7).png').convert_alpha()
        if ship_y_pos <= 80:
            ship_y_pos = 80
    if keys[pygame.K_s]:
        ship_y_pos += ship_movement
        ship_surface = pygame.image.load('SpaceFlight - assets/Sarux03Propel (6).png').convert_alpha()
        if ship_y_pos >= 830:
            ship_y_pos = 830
    if keys[pygame.K_a]:
        ship_x_pos -= ship_movement
        ship_surface = pygame.image.load('SpaceFlight - assets/Sarux03Propel (3).png').convert_alpha()
        if ship_x_pos <= 100:
            ship_x_pos = 100
    if keys[pygame.K_d]:
        ship_x_pos += ship_movement
        ship_surface = pygame.image.load('SpaceFlight - assets/Sarux03Propel (5).png').convert_alpha()
    bg_x_pos -= 3
    bg2_x_pos -= 3
    asteroid_x_pos -= asteroid_speed
    asteroid_rect = asteroid_surface.get_rect(center=(asteroid_x_pos, asteroid_y_pos))
    ship_rect = ship_surface.get_rect(center=(ship_x_pos, ship_y_pos))
    screen.blit(bg_surface, (bg_x_pos, 0))
    screen.blit(bg_surface2, (bg2_x_pos, 0))
    screen.blit(ship_surface, ship_rect)
    screen.blit(asteroid_surface, asteroid_rect)
    if asteroid_x_pos <= -30:
        shape = random.randint(1, 2)
        if shape == 1:
            asteroid_surface = pygame.image.load('SpaceFlight - assets/asteroid.png').convert_alpha()
        else:
            asteroid_surface = pygame.image.load('SpaceFlight - assets/asteroid2.png').convert_alpha()
        asteroid_x_pos = 1500
        asteroid_y_pos = random.randint(30, 850)
        asteroid_speed += .3
        score += 5
        ship_movement += .1
        print(score)
    if bg_x_pos <= -1500:
        bg_x_pos = 0
        bg2_x_pos = 1500
    ship_x_pos += .2
    if ship_rect.colliderect(asteroid_rect):
        ship_surface = pygame.image.load('SpaceFlight - assets/explosion.png').convert_alpha()
        ship_x_pos -= 5
        score -= .5
        asteroid_hit_sound = mixer.Sound('SpaceFlight - assets/asteroidHit.wav')
        asteroid_hit_sound.play()
    text = font.render(str(score), True, GOLD)
    screen.blit(text, (100, 80))
    pygame.display.update()
    clock.tick(160)
