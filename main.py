import random
import sys
import pygame
import time as t

plot = 'A Good Life'
j = 0
pygame.init()
defi = True
screen = pygame.display.set_mode((800, 500))
pygame.display.set_caption('Birthday Bash Adventure!')
CL = pygame.time.Clock()
shown = True

M2 = pygame.mixer.music.load('happy-birthday-jazz-171120.mp3')
pygame.mixer.music.play(-1, 0.0)

I1 = pygame.image.load('Boy_With_Hat.png')
I2 = pygame.transform.scale(pygame.image.load('P.png'), (100, 100))

R1 = I1.get_rect()
R1.center = (400, 250)

R2 = I2.get_rect()
R2.center = (random.randint(100, 700), random.randint(100, 400))

F1 = pygame.font.Font('MotleyForcesRegular-w1rZ3.ttf', 50)
F2 = pygame.font.Font('MotleyForcesRegular-w1rZ3.ttf', 20)
F3 = pygame.font.Font('MotleyForcesRegular-w1rZ3.ttf', 30)
pygame.display.flip()
timedef = 60
while defi:

    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            defi = False
    T5 = F3.render(f'Click 1 For 30 Second Time Limit', True, '#f56767')
    R6 = T5.get_rect()
    R6.center = (300, 100)

    T6 = F3.render(f'Click 2 For 60 Second Time Limit', True, '#ff8945')
    R7 = T6.get_rect()
    R7.center = (300, 200)

    T7 = F3.render(f'Click 3 For 90 Second Time Limit', True, '#fcfc49')
    R8 = T7.get_rect()
    R8.center = (300, 300)

    T8 = F3.render(f'Click 4 For 120 Second Time Limit', True, '#49fc67')
    R9 = T8.get_rect()
    R9.center = (300, 400)

    k = pygame.key.get_pressed()

    if k[pygame.K_1]:
        timedef = 30

    elif k[pygame.K_2]:
        timedef = 60

    elif k[pygame.K_3]:
        timedef = 90

    elif k[pygame.K_4]:
        timedef = 120

    screen.fill('white')
    screen.blit(T5, R6)
    screen.blit(T6, R7)
    screen.blit(T7, R8)
    screen.blit(T8, R9)
    screen.blit(I1, (545, 100))
    screen.blit(pygame.transform.scale(pygame.image.load('Designer (3).png'), (200, 200)), (545, 240))
    pygame.display.update()
    CL.tick(60)

time = t.time()
while shown:

    T1 = F1.render(f'Presents: {j}', True, 'black')
    R3 = T1.get_rect()
    R3.center = (400, 100)

    ET = t.time() - time
    LifeTime = timedef - int(ET)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            shown = False

    x = LifeTime // 60
    y = LifeTime % 60

    T2 = F2.render(f'Time: {x:02}:{y:02}', True, 'black')
    R4 = T2.get_rect()
    R4.center = (657, 100)

    key = pygame.key.get_pressed()

    if key[pygame.K_UP] and R1.y > 0:
        R1.y -= 10

    elif key[pygame.K_DOWN] and R1.y < 267:
        R1.y += 10

    elif key[pygame.K_RIGHT] and R1.x < 584:
        R1.x += 10

    elif key[pygame.K_LEFT] and R1.x > 0:
        R1.x -= 10

    if R1.colliderect(R2):
        R2.center = (random.randint(100, 700), random.randint(100, 400))
        pygame.mixer.Sound('mixkit-achievement-bell-600.wav').play()
        j += 1

    if LifeTime == 0:
        shown = False
        active = True
        while active:
            T3 = F1.render('YOUR GIFT IS:\n', True, (0, 0, 0))
            R5 = T3.get_rect()
            R5.center = (400, 100)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    active = False

            if j > 20 * timedef // 60:
                plot = 'Love'

            if j > 50 * timedef // 60:
                plot = 'Knowledege'

            if j > 100 * timedef // 60:
                plot = 'Success'

            if j > 180 * timedef // 60:
                plot = ('Good Habits, Success, Knowledge, '
                        'and Love')

            if j > 250 * timedef // 60:
                plot = 'An Awesome Life'

            T4 = F2.render(f'{plot}', True, (0, 0, 0))
            R6 = T4.get_rect()
            R6.center = (400, 150)

            screen.fill('white')

            I1 = pygame.transform.scale(I1, (216, 233))
            R1.center = (400, 300)
            screen.blit(T3, R5)
            screen.blit(T4, R6)
            screen.blit(I1, R1)
            pygame.display.update()
            CL.tick(60)

    screen.fill('white')
    screen.blit(I1, R1)
    screen.blit(I2, R2)
    screen.blit(T1, R3)
    screen.blit(T2, R4)
    pygame.display.update()
    CL.tick(60)
