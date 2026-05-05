import pygame
import time
pygame.mixer.init()

pygame.init()

mainscreen=pygame.display.set_mode((800, 800))
pygame.display.set_caption("Birthday project")
song1=pygame.mixer.music.load("nastelbom-happy-birthday-469282.mp3")
pygame.mixer.music.play()
gameloop=True

image1=pygame.image.load("OIP (1).jpg").convert_alpha()
image2=pygame.image.load("OIP (2).jpg").convert_alpha()
image3=pygame.image.load("OIP (3).jpg").convert_alpha()
image4=pygame.image.load("OIP (4).jpg").convert_alpha()
image5=pygame.image.load("OIP (5).jpg").convert_alpha()
smiley=pygame.image.load("pygame smiley picture.png").convert_alpha()
smiley=pygame.transform.scale(smiley,(100,100))

smiley_sprite=smiley.get_rect()
smiley_sprite.center=(400,400)



image1=pygame.transform.scale(image1, (800, 800))
image2=pygame.transform.scale(image2, (800, 800))
image3=pygame.transform.scale(image3, (800, 800))
image4=pygame.transform.scale(image4, (800, 800))
image5=pygame.transform.scale(image5, (800, 800))

images=[image1, image2, image3, image4, image5]


while gameloop:
    for events in pygame.event.get():
        if events.type==pygame.QUIT:
            gameloop=False
            pygame.mixer.music.stop()


    
    for image in images:
        mainscreen.blit(image, (0,0))
        time.sleep(2)
        mainscreen.blit(smiley, smiley_sprite)
        pygame.display.update()


    pygame.display.update()

pygame.quit()