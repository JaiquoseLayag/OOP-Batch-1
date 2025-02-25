import pygame
import random

pygame.init()

WIDTH, HEIGHT = 600, 400
BLOCK_SIZE = 20
WHITE, GREEN, RED, BLACK = (255, 255, 255), (0, 255, 0), (255, 0, 0), (0, 0, 0)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

clock = pygame.time.Clock()
SPEED = 10

snake = [(100, 100)]
snake_dir = (BLOCK_SIZE, 0)
food = (random.randint(0, WIDTH//BLOCK_SIZE - 1) * BLOCK_SIZE,
        random.randint(0, HEIGHT//BLOCK_SIZE - 1) * BLOCK_SIZE)

running = True
while running:
    screen.fill(BLACK)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake_dir != (0, BLOCK_SIZE):
                snake_dir = (0, -BLOCK_SIZE)
            elif event.key == pygame.K_DOWN and snake_dir != (0, -BLOCK_SIZE):
                snake_dir = (0, BLOCK_SIZE)
            elif event.key == pygame.K_LEFT and snake_dir != (BLOCK_SIZE, 0):
                snake_dir = (-BLOCK_SIZE, 0)
            elif event.key == pygame.K_RIGHT and snake_dir != (-BLOCK_SIZE, 0):
                snake_dir = (BLOCK_SIZE, 0)
    
    new_head = (snake[0][0] + snake_dir[0], snake[0][1] + snake_dir[1])
    
    if (new_head in snake or
        new_head[0] < 0 or new_head[0] >= WIDTH or
        new_head[1] < 0 or new_head[1] >= HEIGHT):
        running = False
        
    snake.insert(0, new_head)
    
    if new_head == food:
        food = (random.randint(0, WIDTH//BLOCK_SIZE - 1) * BLOCK_SIZE,
                random.randint(0, HEIGHT//BLOCK_SIZE - 1) * BLOCK_SIZE)
    else:
        snake.pop()
        
    for segment in snake:
        pygame.draw.rect(screen, GREEN, pygame.Rect(segment[0], segment[1], BLOCK_SIZE, BLOCK_SIZE))
        
    pygame.draw.rect(screen, RED, pygame.Rect(food[0], food[1], BLOCK_SIZE, BLOCK_SIZE))
    
    pygame.display.flip()
    clock.tick(SPEED)
    
pygame.quit()