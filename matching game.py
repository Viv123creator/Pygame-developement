import pygame 
pygame.init()

pygame.mixer.init()
bg_music=pygame.mixer.music.load("relaxingtime-piano-music-no8-182820.mp3")

pygame.mixer.music.play(-1)



font=pygame.font.SysFont("Arial", 25)


gameloop=True

mainscreen=pygame.display.set_mode((800,800))
pygame.display.set_caption("Matching game")

ninja=pygame.image.load("Ninga_image-removebg-preview.png")
wizard=pygame.image.load("wisard_image-removebg-preview.png")
archer=pygame.image.load("Archer_image-removebg-preview.png")

sword=pygame.image.load("Sword_image-removebg-preview.png")
bow=pygame.image.load("bow image.jpg")
wand=pygame.image.load("wand_image-removebg-preview.png")

ninja=pygame.transform.scale(ninja, (70,70))
wizard=pygame.transform.scale(wizard, (70,70))
archer=pygame.transform.scale(archer, (70,70))
sword=pygame.transform.scale(sword, (70,70))
bow=pygame.transform.scale(bow, (70,70))
wand=pygame.transform.scale(wand, (70,70))


ninja_sprite=ninja.get_rect()
wizard_sprite=wizard.get_rect()
archer_sprite=archer.get_rect()

sword_sprite=sword.get_rect()
bow_sprite=bow.get_rect()
wand_sprite=wand.get_rect()



ninja_sprite.center=(100,100)
wizard_sprite.center=(100,300)
archer_sprite.center=(100,500)



bow_sprite.center=(500, 100)
wand_sprite.center=(500,300)
sword_sprite.center=(500,500)

line1=False
line2=False
line3=False

ns=False
nb=False
nw=False

ws=False
wb=False
ww=False

aS=False
ab=False
aw=False

font1=pygame.font.SysFont("Arial", 25)
result="correct"


while gameloop:
    for events in pygame.event.get():
        if events.type==pygame.QUIT:
            gameloop=False
            pygame.mixer.music.stop()

        if events.type==pygame.MOUSEBUTTONUP:
            if sword_sprite.collidepoint(events.pos):
                if ns:
                    line1=True
                    nb=False
                    nw=False
                    aS=False
                    ws=False
                    
                    print("ninja line stops")

                if aS:
                    ns=False
                    ws=False
                    ab=False
                    aw=False

                    line2=True
                    print("archer line stops")


                if ws:
                    wb=False
                    ww=False
                    ns=False
                    aS=False

                    line3=True
                    print("wizard line stops")
#bow
            if bow_sprite.collidepoint(events.pos):
                if nb:
                    line1=True
                    ns=False
                    nw=False
                    ab=False
                    wb=False
                    
                    print("ninja line stops")

                if ab:
                    nb=False
                    wb=False
                    aS=False
                    aw=False

                    line2=True
                    print("archer line stops")


                if wb:
                    ww=False
                    ws=False
                    nb=False
                    ab=False

                    line3=True
                    print("wizard line stops")

            if wand_sprite.collidepoint(events.pos):
                if nw:
                    line1=True
                    ns=False
                    nb=False
                    aw=False
                    ww=False
                    
                    print("ninja line stops")

                if aw:
                    nw=False
                    ww=False
                    aS=False
                    ab=False

                    line2=True
                    print("archer line stops")


                if ww:
                    wb=False
                    ws=False
                    nw=False
                    aw=False

                    line3=True
                    print("wizard line stops")
            



        if events.type==pygame.MOUSEBUTTONDOWN:
            if events.button==1:
                if ninja_sprite.collidepoint(events.pos) and line1==False:
                    ns=True
                    nb=True
                    nw=True

                    print("ninja line starts")

                if wizard_sprite.collidepoint(events.pos) and line3==False:
                    ws=True
                    wb=True
                    ww=True
                    print("wizard line starts")
           
                if archer_sprite.collidepoint(events.pos) and line2==False:
                    aS=True
                    ab=True
                    aw=True
                    print("archer line starts")



    mainscreen.fill("black")
    mainscreen.blit(ninja, ninja_sprite)
    mainscreen.blit(wizard, wizard_sprite)
    mainscreen.blit(archer, archer_sprite)
    mainscreen.blit(sword, sword_sprite)
    mainscreen.blit(bow, bow_sprite)
    mainscreen.blit(wand, wand_sprite)
    text1=font.render("Match the following characters to their weapons.", "white", "red")
    mainscreen.blit(text1, (200, 700))
    
    if line1==True:
        
        if ns:
            pygame.draw.line(mainscreen, "green", ninja_sprite.center, sword_sprite.center, width=1)
        if nb:
            pygame.draw.line(mainscreen, "red", ninja_sprite.center, bow_sprite.center, width=1)
            result="incorect"
        if nw:
            pygame.draw.line(mainscreen, "red", ninja_sprite.center, wand_sprite.center, width=1)
            result="incorect"

    #archer  
    if line2==True:
        
        if aS:
            pygame.draw.line(mainscreen, "red", archer_sprite.center, sword_sprite.center, width=1)
            result="incorect"
        if ab:
            pygame.draw.line(mainscreen, "green", archer_sprite.center, bow_sprite.center, width=1)
        if aw:
            pygame.draw.line(mainscreen, "red", archer_sprite.center, wand_sprite.center, width=1)
            result="incorect"
        
#wizard
    if line3==True:
        
        if ws:
            pygame.draw.line(mainscreen, "red", wizard_sprite.center, sword_sprite.center, width=1)
            result="incorect"
        if wb:
            pygame.draw.line(mainscreen, "red", wizard_sprite.center, bow_sprite.center, width=1)
            result="incorect"
        if ww:
            pygame.draw.line(mainscreen, "green", wizard_sprite.center, wand_sprite.center, width=1)

    if line1 and line2 and line3:
        text1=font1.render("{}".format(result), True, "white", "red")
        mainscreen.blit(text1, (300, 50))
        
    
    
    

    pygame.display.update()
pygame.quit()