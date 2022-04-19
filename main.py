import pygame
import time
pygame.init()
class Bird(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() #heriter de la classe sprite et l initialiser
        self.image=pygame.image.load('photo/dove.png')
        self.rect=self.image.get_rect() #le joueur occupe espace de rectangle
        self.rect.x=60 #les cordonnées du rect 
        self.rect.y=190


class Pipe1(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() #heriter de la classe sprite et l initialiser
        self.image=pygame.image.load('photo/pipe1.png')
        self.rect=self.image.get_rect() #le pipe occupe espace de rectangle
        self.rect.x=250 #les cordonnées du rect 
        self.rect.y=210


class Pipe2(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() #heriter de la classe sprite et l initialiser
        self.image=pygame.image.load('photo/pipe2.png')
        self.rect=self.image.get_rect() #le pipe occupe espace de rectangle
        self.rect.x=300 #les cordonnées du rect 
        self.rect.y=-40


pygame.display.set_caption("bird") #generer fenetre
screen=pygame.display.set_mode((390,390)) #taille fenetre
# bg= pygame.image.load('photo/bg.png') #bg
bg1=pygame.image.load('photo/home_page.png')
bird=Bird()
pipe1=Pipe1()
pipe2=Pipe2()
pygame.event.get()
fonctionne=True
playing=True
while fonctionne:
    time.sleep(0.1)#chaque 0.1sec faire la suite
    if not playing:
        screen.blit(bg1, (0,0))#afficher bg sur la fenetre dès point(0,0)
        pygame.display.flip() #mettre a jour l ecran
        for event in pygame.event.get():
            if event.type==pygame.KEYDOWN:
                pipe1=Pipe1()
                pipe2=Pipe2()
                bird=Bird()
                playing=True
            elif event.type == pygame.QUIT: # verifier si l event est fermer la fenetre
                fonctionne=False
                pygame.quit()
    else:
        bird.rect.y=bird.rect.y+7     
        screen.blit(bg1, (0,0))
        screen.blit(pipe1.image,pipe1.rect)
        screen.blit(pipe2.image,pipe2.rect)
        screen.blit(bird.image,bird.rect)
        if pipe1.rect.x<-60:
            pipe1.rect.x=250
        else :
            pipe1.rect.x=pipe1.rect.x-10
        if pipe2.rect.x<-60:
            pipe2.rect.x=300
        else :
            pipe2.rect.x=pipe2.rect.x-10
        #on va vérfier si il y a collusion entre bird et les pipes 
        if  (bird.rect.x-pipe1.rect.x>-18 and pipe1.rect.y-60<bird.rect.y and bird.rect.y<390 and pygame.Rect.colliderect(bird.rect, pipe1.rect)) or (bird.rect.x-pipe2.rect.x>-16 and pipe2.rect.y+190>bird.rect.y and bird.rect.y>0 and pygame.Rect.colliderect(bird.rect, pipe2.rect)):
            playing=False
        pygame.display.flip() #mettre a jour l ecran
        for event in pygame.event.get():#liste contient les evenement faites par l'utilisateur
            if event.type == pygame.QUIT: # verifier si l event est fermer la fenetre
                fonctionne=False
                pygame.quit()
            elif event.type==pygame.KEYDOWN and bird.rect.y>0: 
                bird.rect.y-=30
            