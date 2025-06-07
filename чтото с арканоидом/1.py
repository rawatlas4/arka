import pygame
from random import randint
pygame.init()
win_width = 1200
win_height = 700
window = pygame.display.set_mode((win_width, win_height))
clock = pygame.time.Clock()
with open("2","r",) as file:
    level1 = file.readlines()
class Pryamokytnuk():
    def __init__(self,x,y,width,height,color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.rect = pygame.Rect(self.x,self.y,self.width,self.height)
    def risovka(self):
        pygame.draw.rect(window,self.color,self.rect)
class Ball():
    def __init__(self,x,y,color,radius):
        self.x = x
        self.y = y
        self.color = color
        self.radius = radius
        self.speed_x = 10
        self.speed_y = 10
        self.rect = pygame.Rect(self.x,self.y,self.radius*2,self.radius*2)
    def risovka(self):
        pygame.draw.circle(window,self.color,(self.rect.x,self.rect.y),self.radius)
    def dvizhenie(self):
        self.rect.x+=self.speed_x
        self.rect.y+=self.speed_y
        if ball.rect.y > 699:
            window.blit(im,(0,0))
            pygame.display.update()
            lose.play()
            pygame.time.delay(5000)
            pygame.quit()
            exit()
        if self.rect.x > 1199:
            self.speed_x*=-1
        if self.rect.y < 0:
            self.speed_y*=-1
        if self.rect.x < 0:
            self.speed_x*=-1
a = []
for row,line in enumerate(level1):
    for index,char in enumerate(line):
        if char == '#':
            pygame.draw.rect(window,(255,0,0),(index*100,500,70,50))
            block1 = Pryamokytnuk(index*100,row*100,52,25,(52,78,124))
            a.append(block1)

pygame.mixer.init()
pygame.mixer.music.set_volume(0.3)
pygame.mixer.music.load("game.mp3")
pygame.mixer.music.play(-1)
platforma = Pryamokytnuk(100,500,randint(500,1000),randint(5,15),(0,0,255))
ball = Ball(randint(0,1000),randint(0,500),(0,0,255),randint(5,15))
lose = pygame.mixer.Sound("lose.mp3")
winn = pygame.mixer.Sound("winn.mp3")
otskok = pygame.mixer.Sound("otskok.mp3")
kick = pygame.mixer.Sound("kick.mp3")
im = pygame.transform.scale(pygame.image.load("imagee.jpg"),(win_width,win_height))
fon = pygame.transform.scale(pygame.image.load("fon.jpg"),(win_width,win_height))
win = pygame.image.load("win.jpg")
game = 1
left = False
right = False
while game:
    window.fill((0,0,0))
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            game = 0
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_UP:
                a = []
                for row,line in enumerate(level1):
                    for index,char in enumerate(line):
                        if char == '#':
                            pygame.draw.rect(window,(255,0,0),(index*100,500,70,50))
                            block1 = Pryamokytnuk(index*100,row*100,52,25,(52,78,124))
                            a.append(block1)
            if e.key == pygame.K_LEFT:
                left = True
            if e.key == pygame.K_RIGHT:
                right = True
        if e.type == pygame.KEYUP:
            if e.key == pygame.K_RIGHT:
                right = False
            if e.key == pygame.K_LEFT:
                left = False

    if right:
        platforma.rect.x += 8
    if left:
        platforma.rect.x += -8

    window.blit(fon,(0,0))
    ball.risovka()
    ball.dvizhenie()
    platforma.risovka()
    pygame.draw.line(window,(255,255,0),(0,0),(0,700),10)
    pygame.draw.line(window,(0,255,255),(0,690),(1200,700),10)
    pygame.draw.line(window,(0,255,0),(1199,699),(1199,0),10)
    pygame.draw.line(window,(0,255,0),(1199,0),(0,0),10)

    for i in a:
        i.risovka()
    if platforma.rect.colliderect(ball):
        ball.speed_y *= -1
        otskok.play()
    for block in a:
        if block.rect.colliderect(ball):
            ball.speed_y *=-1
            a.remove(block)
            kick.play()
        if len(a) == 0:
            window.blit(win,(0,0))
            pygame.display.update()
            winn.play()
            pygame.time.delay(5000)
            pygame.quit()
            exit()
    pygame.display.update()
    clock.tick(60)
