import pygame
import random
import sys
from pygame.locals import *

pygame.init()

a = 345
randoml = [100, 600, 345]
randomn = int(random.choice(randoml))
b = 0

surface = pygame.display.set_mode((800, 500))
player = pygame.image.load("graph/player.png").convert()
car = pygame.image.load("graph/car.png").convert()

car_rect = car.get_rect()
player_rect = player.get_rect()

pygame.display.set_caption("Car Racers")

# Set the initial y position of the car to be off the top of the screen
car_y = -car.get_height()

# Set the speed at which the car will move down the screen
car_speed = 0.3

font = pygame.font.Font(None, 36)  # Font for the collision message

running = True
collision_detected = False  # Flag to indicate collision

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                a = 100
            if event.key == K_RIGHT:
                a = 600
            if event.key == K_DOWN:
                a = 345

    car_rect.x = randomn
    car_rect.y = car_y

    player_rect.x = a
    player_rect.y = 300

    if car_rect.colliderect(player_rect):
        collision_detected = True

    if collision_detected:
        # Display collision message within the game window
        message = font.render("You Lost! Press Esc to quit.", True, (255, 0, 0))
        message_rect = message.get_rect(center=(surface.get_width() // 2, surface.get_height() // 2))
        surface.fill((255, 255, 255))
        surface.blit(player, (a, 300))
        surface.blit(car, (randomn, car_y))
        surface.blit(message, message_rect)

        # Check for quit event or Esc key press to exit the game
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            running = False
    else:
        # Update the y position of the car
        car_y += car_speed

        # If the car has moved off the bottom of the screen, reset its y position and randomize its x position
        if car_y > surface.get_height():
            car_y = -car.get_height()
            randomn = int(random.choice(randoml))
            b += 1

        surface.fill((255, 255, 255))
        surface.blit(player, (a, 300))
        surface.blit(car, (randomn, car_y))

        # Render and blit the font surface (score)
        score_surface = font.render("Score: " + str(b), True, (0, 0, 0))
        surface.blit(score_surface, (700, 400))

    pygame.display.flip()

pygame.quit()
