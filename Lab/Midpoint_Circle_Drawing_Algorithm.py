
import pygame

pygame.init()
screen = pygame.display.set_mode((1200,720))
running =True

font = pygame.font.Font(None, 36) 

def midPointAlgo(xinp, yinp, r):
    x = 0
    y = r
    p = 1-r
    while x<=y:
        screen.set_at((y + xinp, x + yinp),"white")
        screen.set_at((x + xinp ,y + yinp ),"white")
        screen.set_at((x + xinp, -y + yinp),"white")
        screen.set_at((y + xinp, -x + yinp),"white")
        screen.set_at((-y + xinp, -x + yinp),"white")
        screen.set_at((-x + xinp, -y + yinp),"white")
        screen.set_at((-x + xinp, y + yinp),"white")
        screen.set_at((-y + xinp, x + yinp),"white")
        
        x+=1
        if p<0:
            p+=2*x+1
        else:
            y-=1
            p+=2*(x-y)+1

    

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill("black")
    midPointAlgo(int(1200/2), int(720/2) ,100)
#  


    pygame.display.update()

pygame.quit()

