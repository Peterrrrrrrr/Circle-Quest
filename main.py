import os
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

# Set up the paths to image files
cwd = os.getcwd()
player_img_path = os.path.join(cwd, "player.png")
enemy_img_path = os.path.join(cwd, "enemy.png")
bullet_img_path = os.path.join(cwd, "bullet.png")

# Load images
player_img = pygame.image.load(player_img_path)
enemy_img = pygame.image.load(enemy_img_path)
bullet_img = pygame.image.load(bullet_img_path)

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

# Handle bullet movement
for i, bullet in enumerate(bullets):
    bullet_x, bullet_y = bullet
    bullet_y -= bullet_speed
    bullets[i] = (bullet_x, bullet_y)

# Handle collision detection
for bullet in bullets:
    bullet_x, bullet_y = bullet
    if (bullet_y < enemy_y + enemy_height and bullet_x > enemy_x and 
        bullet_x < enemy_x + enemy_width):
        bullets.remove(bullet)
        enemy_x = random.randint(0, WIDTH - enemy_width)
        enemy_y = -enemy_height
        score += 1

# Draw everything
screen.fill(BLACK)
screen.blit(player_img, (player_x, player_y))
screen.blit(enemy_img, (enemy_x, enemy_y))
for bullet in bullets:
    screen.blit(bullet_img, bullet)
score_text = font.render(f"Score: {score}", True, WHITE)
screen.blit(score_text, (10, 10))
pygame.display.update()

# Set the framerate
clock.tick(60)
pygame.quit()