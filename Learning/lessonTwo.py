import pygame
import random

pygame.init()

win = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Moja Gra")

run = True

x = 100
y = 100
direction = 1
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    if x >= 490 or x <= 10:
        direction = -direction
        
    win.fill((0, 0, 0))
    x += direction
    y = random.randint(10, 450)
    pygame.draw.circle(win, (128, 0, 128), (x, y), 10, 0)
    pygame.time.delay(100)
    pygame.display.update()
    
    # pygame.draw.rect(win, (255, 0, 0), (10, 30, 100, 100))
    # pygame.draw.circle(win, (128, 0, 128), (60, 200), 50, 0)
    # pygame.draw.line(win, (0, 0, 255), (10, 325), (110, 325), 15)
    # pygame.draw.line(win, (128, 128, 128), (210, 275), (210, 375), 5)
    # font = pygame.font.SysFont('comicsans', 30)
    # label = font.render('Ale ze mnie Pablo Picasso ', 1, (255, 255, 255))
    # win.blit(label, (100, 425))