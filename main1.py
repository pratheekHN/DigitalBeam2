import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 480
SCREEN_HEIGHT = 640
BIRD_WIDTH = 50
BIRD_HEIGHT = 50
PIPE_WIDTH = 70
PIPE_GAP = 200
PIPE_SPEED = 4
BIRD_JUMP = -15

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

# Create screen and clock
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Flappy Bird")
clock = pygame.time.Clock()

# Bird properties
bird_y = SCREEN_HEIGHT / 2
bird_speed = 0

# Pipe properties
pipe_x = SCREEN_WIDTH
pipe_height = random.randint(150, 450)

# Score
score = 0

while True:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_speed = BIRD_JUMP

    # Bird mechanics
    bird_speed += 1  # gravity
    bird_y += bird_speed
    bird_rect = pygame.Rect(50, bird_y, BIRD_WIDTH, BIRD_HEIGHT)
    pygame.draw.rect(screen, BLUE, bird_rect)

    # Pipe mechanics
    pipe_x -= PIPE_SPEED
    top_pipe = pygame.Rect(pipe_x, 0, PIPE_WIDTH, pipe_height)
    bottom_pipe = pygame.Rect(pipe_x, pipe_height + PIPE_GAP, PIPE_WIDTH, SCREEN_HEIGHT)
    pygame.draw.rect(screen, GREEN, top_pipe)
    pygame.draw.rect(screen, GREEN, bottom_pipe)

    if pipe_x < -PIPE_WIDTH:
        pipe_x = SCREEN_WIDTH
        pipe_height = random.randint(150, 450)
        score += 1

    # Collision
    if bird_rect.colliderect(top_pipe) or bird_rect.colliderect(bottom_pipe):
        pygame.quit()
        exit()

    # Score display
    score_text = pygame.font.Font(None, 36).render(str(score), True, (0, 0, 0))
    screen.blit(score_text, (SCREEN_WIDTH / 2, 10))

    pygame.display.flip()
    clock.tick(60)
