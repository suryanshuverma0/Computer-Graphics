import pygame
import sys
import math

# Initialize Pygame
pygame.init()

# Set up display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Rotating Circle Example")

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

def draw_ellipse(xc, yc, rx, ry):
    x = 0
    y = ry
    x1=30
    y1=30+ry
    p1 = round(ry * ry - rx * rx * ry + 0.25 * rx * rx)
    # dx = 2 * ry * ry * x
    # dy = 2 * rx * rx * y
    while (2 * ry * ry * x) <= (2 * rx * rx * y ):
        if(p1 < 0):
            x = x + 1
            y = y
            p1 = p1 + (2 * ry * ry * x) + ry * ry
        else:
            x = x+1
            y = y-1
            p1 = p1 + (2 * ry * ry * x) - (2 * rx * rx * y )+ ry * ry
        screen.set_at(( x + xc , y + yc) , "red") 
        screen.set_at((x + xc , -y + yc) , "red") 
        screen.set_at((-x + xc , y + yc) , "red") 
        screen.set_at((-x + xc , -y + yc) , "red") 

    p2 = round(ry * ry *(x + 1/2) ** 2  + rx * rx * (y-1) ** 2 - rx * rx * ry * ry)
    while y != 0:
        if(p2 >  0):
            x = x 
            y = y-1
            p2 = p2 -  (2 * rx * rx * y )+ rx * rx
        else:
            x = x+1
            y = y-1
            p2 = p2 + (2 * ry * ry * x) - (2 * rx * rx * y )+ rx * rx
        screen.set_at(( x + xc , y + yc) , "red") 
        screen.set_at((x + xc , -y + yc) , "red") 
        screen.set_at((-x + xc , y + yc) , "red") 
        screen.set_at((-x + xc , -y + yc) , "red") 


# Main loop
running = True
angle = 0
angle1=0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill(WHITE)

    # Calculate circle position
    radius = 100
    radius1=130
    center = (width // 2, height // 2)
    x = center[0] + int(radius * math.cos(math.radians(angle)))
    y = center[1] + int(radius * math.sin(math.radians(angle)))
    x1=center[0] + int(radius1 * math.cos(math.radians(angle1)))
    y1=center[1] + int(radius1 * math.sin(math.radians(angle1)))

    # Draw the circle
    pygame.draw.circle(screen, "red", (x, y), 10)
    
    draw_ellipse(width // 2, height // 2, 100, 100)
    pygame.draw.circle(screen,'red',(x1,y1),20)
    draw_ellipse(width // 2 , height // 2 , 130, 130)

    # Update the display
    pygame.display.flip()

    # Rotate the circle
    angle -= 1
    if angle >= 360:
        angle = 0
    angle1 += 1
    if angle1 >= 360:
        angle1 = 0

    # Control the frame rate
    pygame.time.Clock().tick(60)

# Quit Pygame
pygame.quit()
sys.exit()
