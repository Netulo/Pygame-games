import pygame
import random
pygame.init()

white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)

X = 400
Y = 400

display_surface = pygame.display.set_mode((X, Y))
font = pygame.font.Font('freesansbold.ttf', 32)

run = True
while run:
        eq = random.choice(['+', '-', '*', ':'])
        a = random.randint(1, 100)
        b = random.randint(1, 100)
        answ = 0
        if eq == '+':
            answ = a + b
        if eq == '-':
            answ = a - b
        if eq == '*':
            answ = a * b
        if eq == ':':
            answ = a / b
            
            
        text = font.render(f'{a} {eq} {b} = ?', True, green, blue)
        textRect = text.get_rect()
        textRect.center = (X // 2, Y // 2)
        display_surface.blit(text, textRect)
        
        for event in pygame.event.get():
            while True:
                inp = ''
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_0:
                        inp += 0
                    if event.key == pygame.K_1:
                        inp += 1
                    if event.key == pygame.K_2:
                        inp += 2
                    if event.key == pygame.K_3:
                        inp += 3
                    if event.key == pygame.K_4:
                        inp += 4
                    if event.key == pygame.K_5:
                        inp += 5
                    if event.key == pygame.K_6:
                        inp += 6
                    if event.key == pygame.K_7:
                        inp += 7
                    if event.key == pygame.K_8:
                        inp += 8
                    if event.key == pygame.K_9:
                        inp += 9
                    
                if event.type == pygame.KEYDOWN and event.key == pygame.K_KP_ENTER:
                    if int(inp) == answ:
                        text = font.render('Good answear!', True, green, blue)
                    else:
                        text = font.render(f'Bad answer. Answear is {answ}', True, green, blue)
                    
                    textRect = text.get_rect()
                    textRect.center = (X // 2, Y // 2)
                    display_surface.blit(text, textRect)
                    break
            if event.type == pygame.QUIT:
                run = False
            pygame.display.update()
pygame.quit()
        