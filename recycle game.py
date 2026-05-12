import pygame

pygame.init()

mainscreen=pygame.display.set_mode((800,800))
gameloop=True


xcan=100
ycan=100
xbanana=200
ybanana=100
xbattery=300
ybattery=100
xpaperbag=4
ypaperbag=500

score=0



dragging_can=False
dragging_banana=False
dragging_battery=False
dragging_paperbag=False





green_bin=pygame.image.load("green_bin_for_pygame_use-removebg-preview.png")
red_bin=pygame.image.load("red_bin_for_pygame_use-removebg-preview.png")
can=pygame.image.load("can_for_pygame_use-removebg-preview (1).png")
banana_peel=pygame.image.load("banana_peel_png_for_pyame_use-removebg-preview.png")
battery=pygame.image.load("battery_for_pygame_use-removebg-preview.png")
paper_bag=pygame.image.load("paper_bag_for_pygame_use-removebg-preview.png")

green_bin=pygame.transform.scale(green_bin, (100, 100))
red_bin=pygame.transform.scale(red_bin, (100, 100))

can=pygame.transform.scale(can, (50, 50))
banana_peel=pygame.transform.scale(banana_peel, (50, 50))
battery=pygame.transform.scale(battery, (50, 50))
paper_bag=pygame.transform.scale(paper_bag, (50, 50))


green_bin_sprite=green_bin.get_rect()
red_bin_sprite=red_bin.get_rect()






green_bin_sprite.center=(50, 600)
red_bin_sprite.center=(700, 600)


font1=pygame.font.SysFont("Arial", 31)
font2=pygame.font.SysFont("Arial", 25)



while gameloop:
    for events in pygame.event.get():
        if events.type==pygame.QUIT:
            gameloop=False
        
        if events.type==pygame.MOUSEBUTTONDOWN:
            if events.button==1:
                if can_sprite.collidepoint(events.pos):
                    dragging_can=True

                if banana_peel_sprite.collidepoint(events.pos):
                    dragging_banana=True

                if battery_sprite.collidepoint(events.pos):
                    dragging_battery=True

                if paper_bag_sprite.collidepoint(events.pos):
                    dragging_paperbag=True
            
        if events.type==pygame.MOUSEMOTION:
            if dragging_can==True:
                xcan, ycan=pygame.mouse.get_pos()

            if dragging_battery==True:
                xbattery, ybattery=pygame.mouse.get_pos()

            if dragging_banana==True:
                xbanana, ybanana=pygame.mouse.get_pos()

            if dragging_paperbag==True:
                xpaperbag, ypaperbag=pygame.mouse.get_pos()



        if events.type==pygame.MOUSEBUTTONUP:
                dragging_can=False
                dragging_banana=False
                dragging_battery=False
                dragging_paperbag=False
    
    can_sprite=can.get_rect()
    can_sprite.center=(xcan, ycan)
    





    banana_peel_sprite=banana_peel.get_rect()
    battery_sprite=battery.get_rect()
    paper_bag_sprite=paper_bag.get_rect()
    banana_peel_sprite.center=(xbanana, ybanana)
    battery_sprite.center=(xbattery, ybattery)
    paper_bag_sprite.center=(xpaperbag, ypaperbag)
    
    if green_bin_sprite.colliderect(paper_bag_sprite):
        dragging_paperbag=False
        xpaperbag=2000
        ypaperbag=2000
        score=score+1

    if green_bin_sprite.colliderect(can_sprite):
        dragging_can=False
        xcan=2000
        ycan=2000
        score=score+1

    if red_bin_sprite.colliderect(battery_sprite):
        dragging_battery=False
        xbattery=2000
        ybattery=2000
        score=score+1

    if red_bin_sprite.colliderect(banana_peel_sprite):
        dragging_banana=False
        xbanana=2000
        ybanana=2000
        score=score+1
        
    
    
    if red_bin_sprite.colliderect(paper_bag_sprite):
        dragging_paperbag=False
        xpaperbag=2000
        ypaperbag=2000
        score=score-1
        
    if red_bin_sprite.colliderect(can_sprite):
        dragging_can=False
        xcan=2000
        ycan=2000
        score=score-1

    if green_bin_sprite.colliderect(battery_sprite):
        dragging_battery=False
        xbattery=2000
        ybattery=2000
        score=score-1

    if green_bin_sprite.colliderect(banana_peel_sprite):
        dragging_banana=False
        xbanana=2000
        ybanana=2000
        score=score-1
        
    

    mainscreen.fill("black")

    text1=font1.render("score: {}".format(score), False, "green", "white")
    text2=font2.render("Put the recyclable items in the green bin, and the rest in the red bin to earn points!", "green", "white")
    mainscreen.blit(text1, (100, 100))
    mainscreen.blit(text2, (25, 750))

    mainscreen.blit(green_bin, green_bin_sprite)
    mainscreen.blit(red_bin, red_bin_sprite)
    mainscreen.blit(can, can_sprite)
    mainscreen.blit(banana_peel, banana_peel_sprite)
    mainscreen.blit(paper_bag, paper_bag_sprite)
    mainscreen.blit(battery, battery_sprite)


    pygame.display.update()
pygame.quit()