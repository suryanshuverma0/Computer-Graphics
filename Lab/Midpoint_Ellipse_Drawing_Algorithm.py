import pygame
import math
import sys

pygame.init()
screen = pygame.display.set_mode((500, 500))
running = True



def midPointEllipseAlgo(xinp, yinp, rx, ry):
    x = 0
    y = ry

   
    p1 = (ry**2) - (rx**2 * ry) + (0.25 * rx**2)
    dx = 2 * ry**2 * x
    dy = 2 * rx**2 * y

    while dx < dy:
        screen.set_at((xinp + x, yinp + y), "white")
        screen.set_at((xinp - x, yinp + y), "white")
        screen.set_at((xinp + x, yinp - y), "white")
        screen.set_at((xinp - x, yinp - y), "white")

        if p1 < 0:
            x += 1
            dx += 2 * ry**2
            p1 += dx + ry**2
        else:
            x += 1
            y -= 1
            dx += 2 * ry**2
            dy -= 2 * rx**2
            p1 += dx - dy + ry**2

    p2 = (ry**2) * (x + 0.5)**2 + (rx**2) * (y - 1)**2 - (rx**2 * ry**2)

    while y >= 0:
        screen.set_at((xinp + x, yinp + y), "white")
        screen.set_at((xinp - x, yinp + y), "white")
        screen.set_at((xinp + x, yinp - y), "white")
        screen.set_at((xinp - x, yinp - y), "white")

        if p2 > 0:
            y -= 1
            dy -= 2 * rx**2
            p2 += rx**2 - dy
        else:
            y -= 1
            x += 1
            dx += 2 * ry**2
            dy -= 2 * rx**2
            p2 += dx - dy + rx**2

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("black")
    midPointEllipseAlgo(int(250), int(250), 50, 25)
    pygame.display.update()

pygame.quit()
sys.exit()
