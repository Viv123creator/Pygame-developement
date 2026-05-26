import pygame
import time

pygame.init()
pygame.mixer.init()




mainscreen=pygame.display.set_mode((800, 800))
pygame.display.set_caption("Flappy bird!")

background_image=pygame.image.load("flappybird backround.jpg")
background_image=pygame.transform.scale(background_image, (800,800))
background_music=pygame.mixer.music.load("lazarosv-bird-blues-i-365240.mp3")
pygame.mixer.music.play(-1)

flappybird=pygame.image.load("flappybird-removebg-preview.png")
flappybird=pygame.transform.scale(flappybird, (70,70))




pipe2=pygame.image.load("pipe for python flappybbird.png2.png").convert_alpha()
pipe3=pygame.image.load("pipe for python flappybbird.png3.png").convert_alpha()
pipe1=pygame.image.load("pipe for python flappybbird.png2.png").convert_alpha()
pipe4=pygame.image.load("pipe for python flappybbird.png3.png").convert_alpha()


pipe2=pygame.transform.scale(pipe2, (70,400))
pipe3=pygame.transform.scale(pipe3, (70,400))
pipe1=pygame.transform.scale(pipe1, (70,200))
pipe4=pygame.transform.scale(pipe4, (70,600))

flappybird_sprite=flappybird.get_rect()


pipe2_sprite=pipe2.get_rect()
pipe3_sprite=pipe3.get_rect()
pipe1_sprite=pipe1.get_rect()
pipe4_sprite=pipe4.get_rect()


p1x=300
p2x=650
p3x=650
p4x=300

gravity=0.2
fy=500



pipevx=-0.15
score=0
font1=pygame.font.SysFont("Arial", 30)
text1=font1.render("Score:{}".format(score),True, "black", "red")
gameloop=True
gameover=False



while gameloop:
    p1x=p1x+pipevx
    p2x=p2x+pipevx
    p3x=p3x+pipevx
    p4x=p4x+pipevx

    fy=fy+gravity
    


    for events in pygame.event.get():
        if events.type==pygame.QUIT:
            gameloop=False
            pygame.mixer.music.stop()

    pipe2_sprite.center=(p2x,720)
    pipe3_sprite.center=(p3x,140)

    pipe1_sprite.center=(p1x, 720)
    pipe4_sprite.center=(p4x, 140)
    flappybird_sprite.center=(100, fy)

    key=pygame.key.get_pressed()

    if key[pygame.K_SPACE]:
        fy=fy-0.7



    mainscreen.blit(background_image, (0,0))
    mainscreen.blit(flappybird, flappybird_sprite)
    
    mainscreen.blit(pipe3, pipe3_sprite)
    mainscreen.blit(pipe2, pipe2_sprite)
    mainscreen.blit(pipe1, pipe1_sprite)
    mainscreen.blit(pipe4, pipe4_sprite)
    mainscreen.blit(text1, (100, 30))
    


    

    if flappybird_sprite.colliderect(pipe1_sprite):
        pipevx=0
        gameover=True
        
        
        gravity=0
        fy=2000 
        
    if flappybird_sprite.colliderect(pipe2_sprite):
        pipevx=0
        gameover=True
        
        
        gravity=0
        fy=2000 

    if flappybird_sprite.colliderect(pipe3_sprite):
        pipevx=0
        gameover=True
        
        
        gravity=0
        fy=2000

    if flappybird_sprite.colliderect(pipe4_sprite):
        pipevx=0
        gameover=True
        
        
        gravity=0
        fy=2000 


    if gameover==True:
        text2=font1.render("You lose!", "green", "black")
        mainscreen.blit(text2, (400, 400))

    if p1x<0:
        p1x=800
        score=score+1
        text1=font1.render("Score:{}".format(score),True, "black", "red")
        
        

    if p2x<0:
        p2x=800
        score=score+1
        text1=font1.render("Score:{}".format(score),True, "black", "red")

    if p3x<0:
        p3x=800

    if p4x<0:
        p4x=800

    
        
        

    pygame.display.update()

pygame.quit()