import pygame
pygame.init()

screen_width = 800
screen_height = 600

screen = pygame.display.set_mode((screen_width, screen_height))

x = 0
y = 0

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                y += 1
                print(x, y)
            if event.key == pygame.K_s:
                y -= 1
                print(x, y)
            if event.key == pygame.K_d:
                x += 1
                print(x, y)
            if event.key == pygame.K_a:
                x -= 1
                print(x, y)
        
        if event.type == pygame.QUIT:
            run = False
pygame.quit()
    