import pygame
import time

pygame.init()


mainscreen=pygame.display.set_mode((800,800))
pygame.display.set_caption("money clicker")

mainscreen.fill("black")

money=pygame.image.load("money_for_pygame_use-removebg-preview.png")
upgrade=pygame.image.load("upgrade sign for pygame use.jpg")

upgrade=pygame.transform.scale(upgrade, (80, 20))




font1=pygame.font.SysFont("Arial", 31)
font2=pygame.font.SysFont("Arial", 31)

coins=100
text1=font1.render("score: "+str(coins), False, "green", "white")





gameloop=True

uptimes=0

deal=1

while gameloop:
    for events in pygame.event.get():
        if events.type==pygame.QUIT:
            gameloop=False


    if events.type==pygame.MOUSEBUTTONDOWN:
        if events.button==1:
            if money_sprite.collidepoint(events.pos):
                print("moneyclicked")
                print("moneyclicked")
                if deal==1:
                    print("deal 1")
                    print(coins)
                    money_sprite.center=(2000,2000)
                    coins=coins+1
                    text1=font1.render("score: "+str(coins), False, "green", "white")
                    time.sleep(0.2)
                    money_sprite.center=(400,400)
        
                if deal==2:
                    print("deal2")
                    print(coins)
                    money_sprite.center=(2000,2000)
                    coins=coins+2
                    text1=font1.render("score: "+str(coins), False, "green", "white")
                    time.sleep(0.4)
                    money_sprite.center=(400,400)

                if deal==3:
                    
                    money_sprite.center=(2000,2000)
                    coins=coins+4
                    text1=font1.render("score: "+str(coins), False, "green", "white")
                    time.sleep(0.2)
                    money_sprite.center=(400,400)

                if deal==4:
                    
                    money_sprite.center=(2000,2000)
                    coins=coins+8
                    text1=font1.render("score: "+str(coins), False, "green", "white")
                    time.sleep(0.2)
                    money_sprite.center=(400,400)

        
            if upgrade_sprite.collidepoint(events.pos) and deal==1 and coins>100:
                deal=2
                print("upgrade clicked")
                coins=coins-100
                text1=font1.render("score: "+str(coins), False, "green", "white")
                print(coins)
                
                
    money_sprite=money.get_rect()
    upgrade_sprite=upgrade.get_rect()

    money_sprite.center=(400, 400)
    upgrade_sprite.center=(400, 700)
    
   
   
   
   
   
    

    if deal==1:
        text2=font2.render("You need 100 coins", "green", "white")
    if deal==2:
        text2=font2.render("You need 500 coins", "green", "white")
    if deal==3:
        text2=font2.render("You need 2000 coins", "green", "white")
    if deal==4:
        text2=font2.render("You need 10000 coins", "green", "white")





    

    mainscreen.blit(money, money_sprite)
    mainscreen.blit(text1, (100,100))
    mainscreen.blit(text2, (300, 100))
    mainscreen.blit(upgrade, upgrade_sprite)


    pygame.display.update()
pygame.quit()


