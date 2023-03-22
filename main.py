import os
import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the display
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Moving Circle")

# Set up the clock
clock = pygame.time.Clock()

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Set up the circle
circle_radius = 30
circle_border_width = 5
circle_glow_speed = 5
circle_glow_color = RED
circle_color = BLACK
circle_x = WIDTH // 2
circle_y = HEIGHT // 2
circle_speed = 5

# Set up the game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    # Handle circle movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and circle_x > circle_radius:
        circle_x -= circle_speed
    elif keys[pygame.K_RIGHT] and circle_x < WIDTH - circle_radius:
        circle_x += circle_speed
    if keys[pygame.K_UP] and circle_y > circle_radius:
        circle_y -= circle_speed
    elif keys[pygame.K_DOWN] and circle_y < HEIGHT - circle_radius:
        circle_y += circle_speed

    # Handle circle glow animation
    circle_glow_color = (circle_glow_color[1], circle_glow_color[2], circle_glow_color[0])
    circle_color, circle_glow_color = circle_glow_color, circle_color

    # Draw everything
    screen.fill(WHITE)
    pygame.draw.circle(screen, circle_glow_color, (circle_x, circle_y), circle_radius + circle_border_width, circle_border_width)
    pygame.draw.circle(screen, circle_color, (circle_x, circle_y), circle_radius)
    pygame.display.update()

    # Set the framerate
    clock.tick(60)

# Quit Pygame
pygame.quit()
