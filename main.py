#imports
import pygame
import sys
import random

#initilizing pygame
pygame.init()
pygame.mixer.init()

#creating screen
screen = pygame.display.set_mode((1500, 1024))
clock = pygame.time.Clock()

#background surface 1
bg_surface = pygame.image.load('SpaceFlight - assets/space.jpg').convert()
bg_x_pos = 0

#background surface 2
bg_surface2 = pygame.image.load('SpaceFlight - assets/space.jpg').convert()
bg2_x_pos = 1500

#ship surface
ship_surface = pygame.image.load('SpaceFlight - assets/Sarux03Propel (3).png').convert_alpha()
ship_x_pos = 100
ship_y_pos = 300
ship_movement = 5
ship_rect = ship_surface.get_rect(center=(ship_x_pos, ship_y_pos))

#asteroid surface
asteroid_surface = pygame.image.load('SpaceFlight - assets/asteroid.png').convert_alpha()
asteroid_x_pos = 1500
asteroid_y_pos = random.randint(30, 850)
asteroid_speed = 6
asteroid_rect = asteroid_surface.get_rect(center=(asteroid_x_pos, asteroid_y_pos))

#font
font = pygame.font.Font(None, 74)
GOLD = (255, 198, 0)

#variables
score = 0

#game loop
while True:
    #events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
    #key binds
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
        
    #movement of background
    bg_x_pos -= 3
    bg2_x_pos -= 3
    
    #asteroid rect
    asteroid_x_pos -= asteroid_speed
    asteroid_rect = asteroid_surface.get_rect(center=(asteroid_x_pos, asteroid_y_pos))
    
    #ship rect
    ship_rect = ship_surface.get_rect(center=(ship_x_pos, ship_y_pos))
    
    #score text
    text = font.render(str(score), True, GOLD)
    
    #blits
    screen.blit(bg_surface, (bg_x_pos, 0))
    screen.blit(bg_surface2, (bg2_x_pos, 0))
    screen.blit(ship_surface, ship_rect)
    screen.blit(asteroid_surface, asteroid_rect)
    screen.blit(text, (100, 80))
    
    #scoring points/asteroid passing
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
        
    #movement of background
    if bg_x_pos <= -1500:
        bg_x_pos = 0
        bg2_x_pos = 1500
        
    ship_x_pos += .2
    
    #collision between ship and asteroid
    if ship_rect.colliderect(asteroid_rect):
        ship_surface = pygame.image.load('SpaceFlight - assets/explosion.png').convert_alpha()
        ship_x_pos -= 5
        score -= .5
     
    #screen update
    pygame.display.update()
    #fps
    clock.tick(160)
