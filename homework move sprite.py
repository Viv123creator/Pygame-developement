import pygame
mainscreen=pygame.display.set_mode((800, 800))
pygame.display.set_caption("Homework move circle")

gameloop=True

cx=200
cy=200

x=200
y=200




while gameloop==True:
    for events in pygame.event.get():
        if events.type==pygame.QUIT:
            gameloop=False
    mainscreen.fill("white")




    key=pygame.key.get_pressed()
    if key[pygame.K_LEFT]:
        cx=cx-2

    if key[pygame.K_RIGHT]:
        cx=cx+2

    if key[pygame.K_UP]:
        cy=cy-2

    if key[pygame.K_DOWN]:
        cy= cy+2
    
    if key[pygame.K_w]:
        y-=2

    if key[pygame.K_s]:
        y+=2
    
    if key[pygame.K_a]:
        x-=2
    
    if key[pygame.K_d]:
        x+=2


    
    

    pygame.draw.circle(mainscreen, "red", (cx, cy), 20)
    
    image2=pygame.image.load("spacex-rocket-11548703287evbhjvppkz (1).png").convert_alpha()
    image2=pygame.transform.scale(image2, (100, 100))
    
    image2sprite=image2.get_rect()
    image2sprite.center=(x, y)

    mainscreen.blit(image2, image2sprite)

    pygame.display.update()
pygame.quit()