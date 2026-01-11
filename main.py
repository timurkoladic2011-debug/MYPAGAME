import pygame
pygame.init()
WIDTH, HEIGHT = 500,500
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (0,0,255)
RED = (255,0,0)
class sprite:
    def __init__(self,x=10,y=10,width=50,speed=0,image=None,height=50,color=(255,255,255)):
        self.image = image
        self.color = color
        self.rect = pygame.Rect(x,y,width,height)
        self.speed = speed
        self.load_img()
    def draw(self,window):
        if self.image:
            window.blit(self.image,(self.rect.x,self.rect.y))
        else:
            pygame.draw.rect(window,self.color,self.rect)
    def move(self,window):
        key = pygame.key.get_pressed()
        if key[pygame.K_w] and self.rect.x > self.speed:
            self.rect.y -= self.speed
        if key[pygame.K_s] and self.rect.bottom <= window.get_height() - self.speed:
            self.rect.y += self.speed
        if key[pygame.K_a] and self.rect.x > self.speed:
            self.rect.x -= self.speed
        if key[pygame.K_d] and self.rect.right <= window.get_width() - self.speed:
            self.rect.x += self.speed
        
            
    def load_img(self):
        if self.image:
            self.image = pygame.image.load(self.image)
            self.image = pygame.transform.scale(self.image,(self.rect.width,self.rect.height))
window = pygame.display.set_mode((WIDTH,HEIGHT))
clock = pygame.time.Clock()
player = sprite(speed=5,color=RED)
ran = True


while ran:
    window.fill(BLUE)
    player.move(window)
    player.draw(window)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ran =  False 


    pygame.display.flip()

    clock.tick(60)

