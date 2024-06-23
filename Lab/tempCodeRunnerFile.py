import pygame
import sys

pygame.init()

width, height = 800, 600
window = pygame.display.set_mode((width, height))
pygame.display.set_caption('Draw Scaled Line Example')

white = (255, 255, 255)
black = (0, 0, 0)

sx = 1.5

original_start_pos = (25, 25)
original_end_pos = (700, 500)

start_pos = (int(original_start_pos[0] * sx), original_start_pos[1])
end_pos = (int(original_end_pos[0] * sx), original_end_pos[1])

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    window.fill(white)

    pygame.draw.line(window, black, start_pos, end_pos, 5)

    pygame.display.flip()

pygame.quit()
sys.exit()
