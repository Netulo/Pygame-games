import pygame
import random

pygame.init()

win = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Moja Gra")

run = True

score = 0

dinoDiameter = 20
xDino = 200
yDino = 380

obsHeight = 20
obsLength = 20
xObs = 600
yObs = 380

keyUpPressed = False
jump = True
isObsActive = False

font = pygame.font.SysFont('comicsans', 30)
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.time.delay(10)
        
    win.fill((0, 0, 0))
    if keyUpPressed:
        if jump:
            yDino -= 2
            if yDino <= 300:
                jump = False
        else:
            yDino += 2
            if yDino >= 380:
                jump = True
                keyUpPressed = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        keyUpPressed = True
        
    
        
    if isObsActive:
        xObs -= 2
        if xObs < 0:
            isObsActive = False
            score += 1
        pygame.draw.rect(win, (255, 0, 0), (xObs, yObs, obsLength, obsHeight))
    else:
        rand = random.randint(1, 100)
        if rand == 1:
            xObs = 600
            isObsActive = True
    
    
    strScore = 'Score: ' + str(score)
    label = font.render(strScore, 1, (255, 255, 255))
    win.blit(label, (10, 500))
    
    if any(x in list(range(yDino-dinoDiameter, yDino+dinoDiameter)) for x in list(range(yObs, yObs+obsLength))) and any(x in list(range(xDino-dinoDiameter, xDino+dinoDiameter)) for x in list(range(xObs, xObs+20))):
        win.fill((0, 0, 0))
        font = pygame.font.SysFont('comicsans', 100)
        label = font.render(strScore, 1, (255, 255, 255))
        win.blit(label, (300, 300))
        pygame.time.delay(300)
        pygame.quit()
    
    pygame.draw.circle(win, (128, 0, 128), (xDino, yDino), dinoDiameter, 0)
    pygame.draw.line(win, (0, 255, 0), (0, 400), (600, 400), 5)
    font = pygame.font.SysFont('comicsans', 30)
    
    
    pygame.display.update()
    # pygame.draw.rect(win, (255, 0, 0), (10, 30, 100, 100))
    # pygame.draw.circle(win, (128, 0, 128), (60, 200), 50, 0)
    # pygame.draw.line(win, (0, 0, 255), (10, 325), (110, 325), 15)
    # pygame.draw.line(win, (128, 128, 128), (210, 275), (210, 375), 5)
    # font = pygame.font.SysFont('comicsans', 30)
    # label = font.render('Ale ze mnie Pablo Picasso ', 1, (255, 255, 255))
    # win.blit(label, (100, 425))