import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Cinematic Graphics")

# Load background image (optional, else use color)
background_color = (10, 10, 30)

# Font for title
font = pygame.font.SysFont("Arial", 48)
title_surface = font.render("CINEMATIC INTRO", True, (255, 255, 255))
title_alpha = 0

# Star particles
stars = []
for _ in range(100):
    stars.append([random.randint(0, WIDTH), random.randint(0, HEIGHT), random.randint(1, 3)])

clock = pygame.time.Clock()

# Main loop
running = True
while running:
    screen.fill(background_color)

    # Event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw stars
    for star in stars:
        x, y, size = star
        pygame.draw.circle(screen, (255, 255, 255), (x, y), size)
        star[1] += size  # Move down
        if star[1] > HEIGHT:
            star[0] = random.randint(0, WIDTH)
            star[1] = 0

    # Fade in title
    if title_alpha < 255:
        title_alpha += 2
    title_surface.set_alpha(title_alpha)
    screen.blit(title_surface, (WIDTH // 2 - title_surface.get_width() // 2, HEIGHT // 3))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()