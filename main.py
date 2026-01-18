import pygame
from my_class import*

pygame.init()
WIDTH, HEIGHT = 500,500
SIZE = 50
Lvl_map = ["1111111111"
           "1010110101"
           "1000000001"]
bloxs = []
x,y = 0,0
for line in Lvl_map:
    for num in line:
        if num == "1":
            bloxs.append(sprite(x,y,SIZE,SIZE,0,None,BLUE))
        x += SIZE
    y += SIZE
    x = 0

      

BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (0,0,255)
RED = (255,0,0)

window = pygame.display.set_mode((WIDTH,HEIGHT))
clock = pygame.time.Clock()
player = sprite(x=0,y=400,w=100,h=30,speedx=10,speedy=0,color=RED,image=None,)
ball = Ball(x=250,y=250,r=SIZE,speed=5,color=WHITE)

ran = True


while ran:
    window.fill(BLUE)
    player.move(window)
    ball.move(window)
    if ball.rect.colliderect(player.rect):
        ball.dy*=-1
    ball.draw(window)
    for b in bloxs:
        b.draw(window)
        if ball.rect.colliderect(b.rect):
            ball.dx*=-1

    
    player.draw(window)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ran =  False 


    pygame.display.flip()

    clock.tick(60)

