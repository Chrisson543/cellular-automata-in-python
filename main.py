import pygame
import sys
from functions import step

while True:
    try:
        rule = int(input('Enter a number between 0 and 255: '))
        if 0 <= rule <= 255:
            break
        else:
            print('The number must be between 0 and 255.')
    except ValueError:
        print('Invalid input. Please enter a valid integer')


pygame.init()

screen_width = 1500
screen_height = 750
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()

size = 5
length = screen_width // size
current_state = '0' * (length//2) + '1' + '0'*(length//2)

steps = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    if steps <= screen_height // size:
        for x in range(len(current_state)):
            pygame.draw.rect(screen, (255 if 255 * int(current_state[x]) == 0 else 1 , 255 if 255 * int(current_state[x]) == 0 else 1 , 255 if 255 * int(current_state[x]) == 0 else 1 ), pygame.Rect(x * size, steps * size, size-1, size-1))

        current_state = step(current_state, rule)
        steps += 1

    pygame.display.update()
    clock.tick(120)
