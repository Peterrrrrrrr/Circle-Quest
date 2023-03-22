import pygame

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

# Set up the circle
circle_x = WIDTH // 2
circle_y = HEIGHT // 2
circle_radius = 50
circle_fill_color = (255, 0, 0)
circle_fill_color_index = 0
circle_border_color = ORANGE

# Set up the game loop
running = True
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

    # Change the fill color of the circle
    circle_fill_color_index += 1
    if circle_fill_color_index >= 256:
        circle_fill_color_index = 0
    circle_fill_color = (circle_fill_color_index, 0, 0)

    # Draw the screen
    screen.fill(BLACK)
    pygame.draw.circle(screen, circle_fill_color, (circle_x, circle_y), circle_radius)
    pygame.draw.circle(screen, circle_border_color, (circle_x, circle_y), circle_radius, 5)

    # Update the display
    pygame.display.update()

    # Tick the clock
    clock.tick(60)

# Quit Pygame
pygame.quit()
