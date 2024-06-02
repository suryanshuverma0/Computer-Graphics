import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("BRESENHAMS Drawing Algorithm")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

def draw_line(x1, y1, x2, y2, thickness):
    # Bresenham's Line Algorithm
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    sx = 1 if x1 < x2 else -1
    sy = 1 if y1 < y2 else -1
    err = dx - dy

    while True:
        pygame.draw.circle(screen, WHITE, (x1, y1), thickness // 2)

        if x1 == x2 and y1 == y2:
            break
        e2 = 2 * err
        if e2 > -dy:
            err -= dy
            x1 += sx
        if e2 < dx:
            err += dx
            y1 += sy

def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill(BLACK)

        x1, y1 = 20, 20
        x2, y2 = 100, 100
        thickness = 5

        draw_line(x1, y1, x2, y2, thickness)

        pygame.display.flip()

if __name__ == "__main__":
    main()
