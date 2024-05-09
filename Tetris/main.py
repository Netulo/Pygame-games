import pygame
from game import Game

screen = pygame.display.set_mode((700, 600))
pygame.display.set_caption("Tetris")
clock = pygame.time.Clock()


dark_blue = (44, 44, 127)

game = Game()

GAME_UPDATE = pygame.USEREVENT
pygame.time.set_timer(GAME_UPDATE, 200)

game.get_nickname(screen)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and game.game_over == False:
                game.move_left()
            elif event.key == pygame.K_RIGHT and game.game_over == False:
                game.move_right()
            elif event.key == pygame.K_DOWN and game.game_over == False:
                game.move_down()
            elif event.key == pygame.K_SPACE and game.game_over == False:
                game.rotate()
            elif game.game_over == True:
                game.game_over = False
                game.reset()
        if event.type == GAME_UPDATE and game.game_over == False:
            game.move_down()
            
    screen.fill(dark_blue)
    game.draw(screen)
    
    pygame.display.update()
    clock.tick(60)