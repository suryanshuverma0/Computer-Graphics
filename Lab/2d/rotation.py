#rotation
import pygame
import sys
import math

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Line Rotation")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

def draw_line(screen, color, start, end, thickness=1):
    pygame.draw.line(screen, color, start, end, thickness)

def rotate_point(point, angle, origin):
    """
    Rotate a point counterclockwise by a given angle around a pivot point.
    Angle should be in degrees.
    """
    angle_rad = math.radians(angle)
    ox, oy = origin
    px, py = point
    qx = ox + math.cos(angle_rad) * (px - ox) - math.sin(angle_rad) * (py - oy)
    qy = oy + math.sin(angle_rad) * (px - ox) + math.cos(angle_rad) * (py - oy)
    return round(qx), round(qy)

def main():
    start = (100, 100)
    end = (400, 100)
    line = [start, end]
    

    rotation_angle = 45  
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill(BLACK)
        
        draw_line(screen, WHITE, line[0], line[1], 2)
        
    
        rotated_end = rotate_point(end, rotation_angle, start)
        
        draw_line(screen, WHITE, start, rotated_end, 2)
        
        pygame.display.flip()

if __name__ == "__main__":
    main()
