import pygame
import random

# Colors
white = (255, 250, 218)
red = (255, 0, 0)
black = (0, 0, 0)
blue = (0, 0, 255)

# Initialize Pygame
pygame.init()

# Game window
screen_width = 1200
screen_height = 500
gameWindow = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Snake Game With Abhishek")

# Clock & FPS
clock = pygame.time.Clock()
fps = 30

# Fonts
font = pygame.font.SysFont(None, 35)
large_font = pygame.font.SysFont(None, 55)

# Utility to show text
def display_text(text, color, x, y, font_obj=font):
    screen_text = font_obj.render(text, True, color)
    gameWindow.blit(screen_text, [x, y])

# Generate new food position
def get_new_food_pos():
    return (
        random.randint(14, (screen_width - 30) // 10) * 10,
        random.randint(14, (screen_height - 30) // 10) * 10
    )

# Game loop
def game_loop():
    # Snake properties
    snake_pos = [100, 50]
    snake_body = []
    snake_size = 20
    snake_length = 1
    velocity_x, velocity_y = 0, 0
    snake_speed = 7

    # Score and level
    score = 0
    level = 1
    level_up_score = 5

    # Food
    food_size = 20
    food_pos = get_new_food_pos()

    game_exit = False
    game_over = False

    while not game_exit:
        if game_over:
            gameWindow.fill(white)
            display_text("GAME OVER!", red, screen_width // 2 - 120, screen_height // 2 - 50, large_font)
            display_text(f"Score: {score}", black, screen_width // 2 - 50, screen_height // 2, font)
            display_text("Press R to Play Again or Q to Quit", black, screen_width // 2 - 200, screen_height // 2 + 40)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_exit = True
                    game_over = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        game_loop()  # Restart game
                    elif event.key == pygame.K_q:
                        game_exit = True
                        game_over = False
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_exit = True
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT and velocity_x == 0:
                        velocity_x, velocity_y = snake_speed, 0
                    elif event.key == pygame.K_LEFT and velocity_x == 0:
                        velocity_x, velocity_y = -snake_speed, 0
                    elif event.key == pygame.K_UP and velocity_y == 0:
                        velocity_x, velocity_y = 0, -snake_speed
                    elif event.key == pygame.K_DOWN and velocity_y == 0:
                        velocity_x, velocity_y = 0, snake_speed

            # Update snake position
            snake_pos[0] += velocity_x
            snake_pos[1] += velocity_y

            # Check boundary collision
            if (snake_pos[0] < 10 or snake_pos[0] > screen_width - 10 - snake_size or
                snake_pos[1] < 10 or snake_pos[1] > screen_height - 10 - snake_size):
                game_over = True

            # Check food collision
            if abs(snake_pos[0] - food_pos[0]) < snake_size and abs(snake_pos[1] - food_pos[1]) < snake_size:
                food_pos = get_new_food_pos()
                snake_length += 1
                score += 1

                if score % level_up_score == 0:
                    level += 1
                    snake_speed += 1

            # Snake body update
            snake_body.append(list(snake_pos))
            if len(snake_body) > snake_length:
                del snake_body[0]

            # Drawing
            gameWindow.fill(white)
            pygame.draw.rect(gameWindow, blue, [10, 10, screen_width - 20, screen_height - 20], 4)

            # Draw snake
            for segment in snake_body:
                pygame.draw.rect(gameWindow, black, [segment[0], segment[1], snake_size, snake_size])

            # Draw food
            pygame.draw.rect(gameWindow, red, [food_pos[0], food_pos[1], food_size, food_size])

            # Score and level
            display_text(f"Score: {score}", black, 20, 20)
            display_text(f"Level: {level}", black, 20, 50)

            pygame.display.update()
            clock.tick(fps)

# Start the game
game_loop()
pygame.quit()
quit()
