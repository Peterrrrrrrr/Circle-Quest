import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the display
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Shooter")

# Set up the clock
clock = pygame.time.Clock()

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Load images
player_img = pygame.image.load("player.png")
enemy_img = pygame.image.load("enemy.png")
bullet_img = pygame.image.load("bullet.png")

# Set up the player
player_speed = 5
player_width, player_height = player_img.get_size()
player_x = WIDTH // 2 - player_width // 2
player_y = HEIGHT - player_height - 10

# Set up the enemy
enemy_speed = 3
enemy_width, enemy_height = enemy_img.get_size()
enemy_x = random.randint(0, WIDTH - enemy_width)
enemy_y = -enemy_height

# Set up the bullets
bullet_speed = 10
bullet_width, bullet_height = bullet_img.get_size()
bullets = []

# Set up the score
score = 0
font = pygame.font.Font(None, 36)

# Set up the game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # Fire a bullet
                bullet_x = player_x + player_width // 2 - bullet_width // 2
                bullet_y = player_y - bullet_height
                bullets.append((bullet_x, bullet_y))

    # Handle player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    elif keys[pygame.K_RIGHT] and player_x < WIDTH - player_width:
        player_x += player_speed

    # Handle enemy movement
    enemy_y += enemy_speed
    if enemy_y > HEIGHT:
        enemy_x = random.randint(0, WIDTH - enemy_width)
        enemy_y = -enemy_height
        score += 10

    # Handle bullet movement
    for bullet in bullets:
        bullet_x, bullet_y = bullet
        bullet_y -= bullet_speed
        if bullet_y < 0:
            bullets.remove(bullet)
        else:
            # Check for collisions with enemy
            if enemy_x < bullet_x < enemy_x + enemy_width and enemy_y < bullet_y < enemy_y + enemy_height:
                enemy_x = random.randint(0, WIDTH - enemy_width)
                enemy_y = -enemy_height
                bullets.remove(bullet)
                score += 100

    # Draw the background
    screen.fill(BLACK)

    # Draw the player
    screen.blit(player_img, (player_x, player_y))

    # Draw the enemy
    screen.blit(enemy_img, (enemy_x, enemy_y))

    # Draw the bullets
    for bullet in bullets:
        bullet_x, bullet_y = bullet
        screen.blit(bullet_img, (bullet_x, bullet_y))

    # Draw the score
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

    # Update the display
    pygame.display.flip()

    # Wait for the next frame
    clock.tick(60)

# Clean up Pygame
