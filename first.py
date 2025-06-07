import pygame

# Initialize Pygame
pygame.init()

# Create the game window
gameWindow = pygame.display.set_mode((1200, 500))
pygame.display.set_caption("My Game") #title of the gam

#varible in game

game_exit = False # to close the game
game_over = False # for the gamer

#game loop
while not game_exit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_exit = True
        
        
        # Only handle key presses once
        if event.type == pygame.KEYDOWN:
            print(f"Key pressed: {pygame.key.name(event.key)}")
        
        if event.type == pygame.KEYUP:
            print(f"Key released: {pygame.key.name(event.key)}")
     
    #background
    gameWindow.fill((255,25,5))  
    # ✅ THIS LINE IS NECESSARY TO REFLECT CHANGES ON SCREEN
    pygame.display.update()      


pygame.quit()
quit()