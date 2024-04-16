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
    display_surface.fill(white)

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

    pygame.display.update()

    inp = ''
    waiting_for_enter = True
    while waiting_for_enter:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                waiting_for_enter = False
            elif event.type == pygame.KEYDOWN:
                if event.key in [pygame.K_KP_ENTER, pygame.K_RETURN]:
                    if inp:
                        waiting_for_enter = False
                elif event.key == pygame.K_MINUS:
                    inp += '-'
                elif event.key == pygame.K_PERIOD:
                    inp += '.'
                elif pygame.K_0 <= event.key <= pygame.K_9:
                    inp += str(event.key - pygame.K_0)

        pygame.draw.rect(display_surface, white, (150, 250, 100, 50))

        input_text = font.render(inp, True, green, blue)
        input_textRect = input_text.get_rect()
        input_textRect.center = (X // 2, Y // 2 + 50)
        display_surface.blit(input_text, input_textRect)

        pygame.display.update()

    if run:
        if float(inp) == answ:
            result_text = font.render('Good answer!', True, green, blue)
        else:
            result_text = font.render(f'Bad answer. Answer is {answ}', True, green, blue)
        result_textRect = result_text.get_rect()
        result_textRect.center = (X // 2, Y // 2 + 100)
        display_surface.blit(result_text, result_textRect)
        pygame.display.update()

        pygame.time.delay(2000)

pygame.quit()
