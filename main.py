import pygame
import time
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
ORANGE = (255, 128, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)

# Set up the main circle
circle_x = WIDTH // 2
circle_y = HEIGHT // 2
circle_radius = 50
circle_fill_color = (255, 0, 0)
circle_border_color = ORANGE

# Set up the list of small circles
small_circles = []

# Set up the points system
points = 0
font = pygame.font.Font(None, 36)

# Set up the game loop
running = True
start_time = time.time()
spawn_time = random.randint(1, 5)  # Spawn first small circle after 1-5 seconds
last_spawn_time = start_time
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Handle circle movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and circle_x > circle_radius:
        circle_x -= 5
    elif keys[pygame.K_RIGHT] and circle_x < WIDTH - circle_radius:
        circle_x += 5
    elif keys[pygame.K_UP] and circle_y > circle_radius:
        circle_y -= 5
    elif keys[pygame.K_DOWN] and circle_y < HEIGHT - circle_radius:
        circle_y += 5

    # Check for collisions with small circles
    for small_circle in small_circles:
        distance = ((circle_x - small_circle[0]) ** 2 + (circle_y - small_circle[1]) ** 2) ** 0.5
        if distance <= circle_radius + small_circle[2]:
            small_circles.remove(small_circle)
            points += 1

    # Spawn a new small circle randomly
    current_time = time.time()
    if current_time - last_spawn_time >= spawn_time:
        small_circle_x = random.randint(circle_radius, WIDTH - circle_radius)
        small_circle_y = random.randint(circle_radius, HEIGHT - circle_radius)
        small_circle_radius = random.randint(5, 20)
        small_circle = (small_circle_x, small_circle_y, small_circle_radius)
        small_circles.append(small_circle)
        spawn_time = random.randint(1, 5)
        last_spawn_time = current_time

    # Fill the background
    screen.fill(BLACK)

    # Draw the small circles
    for small_circle in small_circles:
        pygame.draw.circle(screen, YELLOW, small_circle[:2], small_circle[2], 0)

    # Draw the main circle
    pygame.draw.circle(screen, circle_fill_color, (circle_x, circle_y), circle_radius, 0)
    pygame.draw.circle(screen, circle_border_color, (circle_x, circle_y), circle_radius, 5)

    # Draw the points
    text = font.render("Points: " + str(points), True, WHITE)
    screen.blit(text, (10, 10))

    # Update the display
    pygame.display.update()

    # Tick the clock
    clock.tick(60)

# Quit Pygame
pygame.quit()
