import pygame
import random
import time


pygame.init()
pygame.mixer.init()

mainscreen=pygame.display.set_mode((800, 800))

gameloop=True

pygame.display.set_caption("Space invaders")

background_image=pygame.image.load("pixel space background for pygame use.jpg")
spaceship_image=pygame.image.load("spaceship_for_pygame_use-removebg-preview.png").convert_alpha()
UFO_image=pygame.image.load("UFO_for_pygame_use-removebg-preview.png").convert_alpha()
meteor_image=pygame.image.load("meteor_for_pygame_use-removebg-preview.png").convert_alpha()
dot_image=pygame.image.load("DOT_PNG_FOR_PYGAME-removebg-preview.png")



spaceship_image=pygame.transform.scale(spaceship_image, (60, 60))
UFO_image=pygame.transform.scale(UFO_image, (60, 60))
meteor_image=pygame.transform.scale(meteor_image, (60, 60))
dot_image=pygame.transform.scale(dot_image, (1,1))

font1=pygame.font.SysFont("Arial", 30)


spaceship_sprite=spaceship_image.get_rect()
UFO_sprite=UFO_image.get_rect()
meteor_sprite=meteor_image.get_rect()
meteor_sprite2=meteor_image.get_rect()
dot_sprite=dot_image.get_rect()

sx=400
sy=700
ux=150
uy=50

spaceship_sprite.center=(sx, sy)
UFO_sprite.center=(ux, uy)



background_image=pygame.transform.scale(background_image,(800, 800))



background_music=pygame.mixer.music.load("space music.mp3")

pygame.mixer.music.play(-1)
m1y=50
m2y=300
m1x=300
m2x=700

dy=0
dx=0

move=True

velocity=0.5
d_velocity=0.1


i=0



while gameloop:
   
    m1y=m1y+velocity
    m2y=m2y+velocity
    dy=dy+d_velocity
    for events in pygame.event.get():
        if events.type==pygame.QUIT:
            gameloop=False
            pygame.mixer.music.stop()
    meteor_sprite.center=(m1x, m1y)
    meteor_sprite2.center=(m2x, m2y)
    dot_sprite.center=(dx, dy)

    mainscreen.blit(background_image, (0,0))
    mainscreen.blit(spaceship_image, spaceship_sprite)
    mainscreen.blit(UFO_image, UFO_sprite)
    mainscreen.blit(meteor_image, meteor_sprite)
    mainscreen.blit(meteor_image, meteor_sprite2)
    mainscreen.blit(dot_image, dot_sprite)

    spaceship_sprite.center=(sx, sy)

    key=pygame.key.get_pressed()

    if key[pygame.K_LEFT] and move==True:
        sx=sx-1

    if key[pygame.K_RIGHT]and move==True:
        sx=sx+1

    if key[pygame.K_UP]and move==True:
        sy=sy-1

    if key[pygame.K_DOWN]and move==True:
        sy=sy+1

    if spaceship_sprite.colliderect(meteor_sprite) or spaceship_sprite.colliderect(meteor_sprite2):
        velocity=0
        
        text1=font1.render("You lose!", "red", "white")
        mainscreen.blit(text1, (400, 400))
        spaceship_sprite.center=(2000, 2000)
        move=False


    if spaceship_sprite.colliderect(UFO_sprite):
        velocity=0
        
        spaceship_sprite.center=(2000, 2000)
        move=False
        text2=font1.render("You Win!", "green", "white")
        mainscreen.blit(text2, (400, 400))
    
    if m1y>800:
        m1y=0
        m1x=random.randint(100, 700)
    
    if m2y>800:
        m2y=0
        m2x=random.randint(100, 700)

    if dy>800:
        dy=0
        ux=random.randint(100, 700)
        UFO_sprite.center=(ux, uy)

    
    pygame.display.flip()

pygame.quit()
