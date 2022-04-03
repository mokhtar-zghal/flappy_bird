import pygame
import time
pygame.init()
class Bird(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() #heriter de la classe sprite et l initialiser
        self.velocity=2
        self.image=pygame.image.load('photo/dove.png')
        self.rect=self.image.get_rect() #le joueur occupe espace de rectangle
        self.rect.x=60 #les cordonnées du rect 
        self.rect.y=190

class Pipe1(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() #heriter de la classe sprite et l initialiser
        self.velocity=2
        self.image=pygame.image.load('photo/pipe1.png')
        self.rect=self.image.get_rect() #le pipe occupe espace de rectangle
        self.rect.x=250 #les cordonnées du rect 
        self.rect.y=210
    
class Pipe2(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() #heriter de la classe sprite et l initialiser
        self.velocity=2
        self.image=pygame.image.load('photo/pipe2.png')
        self.rect=self.image.get_rect() #le pipe occupe espace de rectangle
        self.rect.x=300 #les cordonnées du rect 
        self.rect.y=-40




pygame.display.set_caption("bird") #generer fenetre
screen=pygame.display.set_mode((390,390)) #taille fenetre
bg= pygame.image.load('photo/bg.png') #bg
bird=Bird()
pipe1=Pipe1()
pipe2=Pipe2()
pygame.event.get()
fonctionne=True
while fonctionne:
    time.sleep(0.1)
    
    
    
    #pipe2.rect.x-=4
    bird.rect.y=bird.rect.y+7 ##############
    
    screen.blit(bg, (0,0))
    screen.blit(pipe1.image,pipe1.rect)
    screen.blit(pipe2.image,pipe2.rect)
    screen.blit(bird.image,bird.rect)
    #print(pipe1.rect.left)
    if pipe1.rect.x<-60:
        pipe1.rect.x=250
        #pipe1.rect.y=random(....)
    else :
        pipe1.rect.x=pipe1.rect.x-10
    if pipe2.rect.x<-60:
        pipe2.rect.x=300
        #pipe1.rect.y=random
    else :
        pipe2.rect.x=pipe2.rect.x-10
    # if pygame.Rect.colliderect(bird.rect, pipe1.rect):
    #     continue
        # fonctionne=False
        # pygame.quit()
    if  pygame.Rect.colliderect(bird.rect, pipe1.rect):
        fonctionne=False
        pygame.quit()
    if  pygame.Rect.colliderect(bird.rect, pipe2.rect):
        fonctionne=False
        pygame.quit()
    pygame.display.flip() #mettre a jour l ecran
    #print(pipe2.rect.x)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # verifier si l event est fermer la fenetre
            fonctionne=False
            pygame.quit()
        elif event.type==pygame.KEYDOWN and bird.rect.y>0: #and bird.rect.y<360:
            bird.rect.y-=30     
        # elif bird.rect.y>390:
        #     fonctionne=False
        #     pygame.quit()
        