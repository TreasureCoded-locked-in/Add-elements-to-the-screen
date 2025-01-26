import pygame

# Initialize pygame
pygame.init()

# Set the dimensions of the screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("My Game")

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with white
    screen.fill(white)

    # Draw a rectangle
    pygame.draw.rect(screen, red, (100, 100, 200, 150))

    # Draw text
    font = pygame.font.Font(None, 36)
    text = font.render("Hello, Pygame!", True, black)
    text_rect = text.get_rect(center=(screen_width // 2, screen_height // 2))
    screen.blit(text, text_rect)

    # Update the display
    pygame.display.update()

# Quit pygame
pygame.quit()