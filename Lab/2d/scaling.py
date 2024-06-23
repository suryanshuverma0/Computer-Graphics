#scaling
import pygame
import sys

pygame.init()

width, height = 800, 600
window = pygame.display.set_mode((width, height))
pygame.display.set_caption('Draw Scaled Line Example')

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)  # Color for the original line
blue = (0, 0, 255)  # Color for the scaled line

sx =float( input("Enter the sx"))
sy = float(input("Enter the sy"))

original_start_pos = (25, 25)
original_end_pos = (700, 500)

start_pos = (int(original_start_pos[0] * sx), int(original_start_pos[1] * sy))
end_pos = (int(original_end_pos[0] * sx), int(original_end_pos[1] * sy))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    window.fill(white)

    # Draw the original line
    pygame.draw.line(window, red, original_start_pos, original_end_pos, 5)
    # Draw the scaled line
    pygame.draw.line(window, blue, start_pos, end_pos, 5)

    pygame.display.flip()

pygame.quit()
sys.exit()
