import pygame 
pygame.init()
screen=pygame.display.set_mode((500, 500))
pygame.display.set_caption("My first screen!")
gameloop=True

while gameloop:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            gameloop=False
        screen.fill("blue")
        pygame.display.flip()



pygame.quit()