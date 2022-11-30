def main():
    import pygame
    import random
    import sys
    import json
    import time
    import button

    pygame.init()

    screen = pygame.display.set_mode((800,600))
    pygame.display.set_caption("Coffee hop by @itssw4ggy")
    icon = pygame.image.load("Assets\coffeeBeanU.png")
    pygame.display.set_icon(icon)

    # Coffee Beans

    CB1y = random.randint(0,536)
    CB1x = random.randint(0,736)
    CB2y = random.randint(0,536)
    CB2x = random.randint(0,736)
    CB3y = random.randint(0,536)
    CB3x = random.randint(0,736)
    CB1skin = random.randint(1,3)
    CB2skin = random.randint(1,3)
    CB3skin = random.randint(1,3)
    CB1imagR = pygame.image.load("Assets\coffeeBeansR.png")
    CB1imagL = pygame.image.load("Assets\coffeeBeansL.png")
    CB1imagD = pygame.image.load("Assets\coffeeBeansD.png")
    CB2imagR = pygame.image.load("Assets\coffeeBeansR.png")
    CB2imagL = pygame.image.load("Assets\coffeeBeansL.png")
    CB2imagD = pygame.image.load("Assets\coffeeBeansD.png")
    CB3imagR = pygame.image.load("Assets\coffeeBeansR.png")
    CB3imagL = pygame.image.load("Assets\coffeeBeansL.png")
    CB3imagD = pygame.image.load("Assets\coffeeBeansD.png")
    SCB1y = random.randint(0,536)
    SCB1x = random.randint(0,736)
    SCB2y = random.randint(0,536)
    SCB2x = random.randint(0,736)
    SCB3y = random.randint(0,536)
    SCB3x = random.randint(0,736)
    SCB1skin = random.randint(1,3)
    SCB2skin = random.randint(1,3)
    SCB3skin = random.randint(1,3)
    SCB1imagR = pygame.image.load("Assets\CoffeeBeanR.png")
    SCB1imagL = pygame.image.load("Assets\CoffeeBeanL.png")
    SCB1imagU = pygame.image.load("Assets\CoffeeBeanU.png")
    SCB2imagR = pygame.image.load("Assets\CoffeeBeanR.png")
    SCB2imagL = pygame.image.load("Assets\CoffeeBeanL.png")
    SCB2imagU = pygame.image.load("Assets\CoffeeBeanU.png")
    SCB3imagR = pygame.image.load("Assets\CoffeeBeanR.png")
    SCB3imagL = pygame.image.load("Assets\CoffeeBeanL.png")
    SCB3imagU = pygame.image.load("Assets\CoffeeBeanU.png")
    SCB1Img = SCB1imagR
    SCB2Img = SCB2imagR
    SCB3Img = SCB3imagR
    CB1Img = CB1imagR
    CB2Img = CB2imagR
    CB3Img = CB3imagR
    CB1 = CB1Img.get_rect()
    CB2 = CB2Img.get_rect()
    CB3 = CB3Img.get_rect()
    SCB1 = SCB1Img.get_rect()
    SCB2 = SCB2Img.get_rect()
    SCB3 = SCB3Img.get_rect()
    CB1.x = CB1x
    CB1.y = CB1y
    CB2.x = CB1x
    CB2.y = CB2y
    CB3.x = CB3x
    CB3.y = CB3y
    SCB1.x = SCB1x
    SCB1.y = SCB1y
    SCB2.x = SCB2x
    SCB2.y = SCB2y
    SCB3.x = SCB3x
    SCB3.y = SCB3y
    if CB1skin == 1:
        CB1Img = CB1imagR
    if CB1skin == 2:
        CB1Img = CB1imagL
    if CB1skin == 3:
        CB1Img = CB1imagD
    if CB2skin == 1:
        CB2Img = CB2imagR
    if CB2skin == 2:
        CB2Img = CB2imagL
    if CB2skin == 3:
        CB2Img = CB2imagD
    if CB3skin == 1:
        CB3Img = CB3imagR
    if CB3skin == 2:
        CB3Img = CB3imagL
    if CB3skin == 3:
        CB3Img = CB3imagD
    if SCB1skin == 1:
        SCB1Img = SCB1imagR
    if SCB1skin == 2:
        SCB1Img = SCB1imagL
    if SCB1skin == 3:
        SCB1Img = SCB1imagU
    if SCB2skin == 1:
        SCB2Img = SCB2imagR
    if SCB2skin == 2:
        SCB2Img = SCB2imagL
    if SCB2skin == 3:
        SCB2Img = SCB2imagU
    if SCB3skin == 1:
        SCB3Img = SCB3imagR
    if SCB3skin == 2:
        SCB3Img = SCB3imagL
    if SCB3skin == 3:
        SCB3Img = SCB3imagU

    # Font and score

    with open('Assets\DataFiles\Highscore') as highscoreFile:
        highscore = json.load(highscoreFile)

    font = pygame.font.Font('Assets\Bubblegum.ttf', 22)
    menuFont = pygame.font.Font('Assets\Bubblegum.ttf', 48)
    dedFont = pygame.font.Font('Assets\Bubblegum.ttf', 32)

    def Score():
        score_value = font.render('Score: ' + str(score), True, (255,255,255))
        screen.blit(score_value, (345, 20))
    
    def high_score():
        highscore_value = font.render('Highscore: ' + str(highscore), True, (255,255,255))
        screen.blit(highscore_value, (323, 40))
    
    Three = menuFont.render('3', True, (255,255,255))
    Two = menuFont.render('2', True, (255,255,255))
    One = menuFont.render('1', True, (255,255,255))

    score = 0

    startPause = False
    counter = 0

    update = 0

    # Player

    dedPlayerLImg = pygame.image.load("Assets\dedCoffeeL.png")
    dedPlayerRImg = pygame.image.load("Assets\dedCoffeeR.png")
    playerLImg = pygame.image.load("Assets\CoffeeL.png")
    playerRImg = pygame.image.load("Assets\CoffeeR.png")
    playerImg = playerRImg
    dedplayerImg = dedPlayerRImg
    player = playerImg.get_rect()
    player.x = 200
    player.y = 300
    vel = 1
    turnVel = 1
    turn = False
    turnImg = True
    jump = False
    ded = False
    turning = False

    # Loading screen
    loadingTime = random.randint(2,5)

    def lodingScreen():
        Draw = menuFont.render('Loading...', True, (255,255,255))
        screen.blit(Draw,(300,350))
    
    timer = -1

    # Ded screen
    def dedScore():
        Font = dedFont.render('Score : ' + str(score), True, (255,255,255))
        screen.blit(Font,(150, 250))
    
    def dedHighscore():
        Font = dedFont.render('Highscore : ' + str(highscore), True, (255,255,255))
        screen.blit(Font, (150, 320))
    
    def clickTo():
        Font = menuFont.render('Left Click to go to menu', True, (255,255,255))
        screen.blit(Font, (125,450))
    
    def Stats():
        Font = menuFont.render('Your stats', True, (255,255,255))
        screen.blit(Font, (270, 40))

    # Buttons
    startButtonImg = pygame.image.load("Assets\Buttons\play.png")
    shopButtonImg = pygame.image.load("Assets\Buttons\shopButton.png")
    ButtonImg = pygame.image.load("Assets\Buttons\quit.png")

    startButton = button.Button(368, 350, startButtonImg, 1)
    shopButton = button.Button(20, 520, shopButtonImg, 1)
    Button = button.Button(30, 30, ButtonImg, 1)

    # Menu coffee
    menuCoffee = pygame.image.load("Assets\straightCup.png")

    # Shop
    shop = False

    menu = True
    while menu:

        screen.fill((130,130,130))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                with open("Assets\DataFiles\Highscore", "w") as highscoreFile:
                    json.dump(highscore,highscoreFile)
                pygame.quit()
                sys.exit()
        
        if startButton.draw(screen):
            menu = False
        if shopButton.draw(screen):
            shop = True
            menu = False

        screen.blit(menuCoffee,(330, 150))
        
        pygame.display.update()
    runShop = True
    while runShop:

        if shop == False:
            runShop = False
        
        screen.fill((0,0,0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                with open("Assets\DataFiles\Highscore", "w") as highscoreFile:
                    json.dump(highscore,highscoreFile)
                pygame.quit()
                sys.exit()

        if Button.draw(screen):
            main()
        
        pygame.display.update()

    LoadingScreen = True
    while LoadingScreen:

        screen.fill((30,155,227))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                with open("Assets\DataFiles\Highscore", "w") as highscoreFile:
                    json.dump(highscore,highscoreFile)
                pygame.quit()
                sys.exit()
        
        if timer == 0:
            time.sleep(loadingTime)
            LoadingScreen = False
        
        lodingScreen()

        pygame.display.update()
        timer += 1

    running = True
    while running:

        screen.fill((30,155,227))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                with open("Assets\DataFiles\Highscore", "w") as highscoreFile:
                    json.dump(highscore,highscoreFile)
                pygame.quit()
                sys.exit()
        
        userInput = pygame.key.get_pressed()
        if userInput[pygame.K_SPACE] and ded == False:
            vel = 1
            jump = True
        if jump == True:
            player.y -= 2*vel
            vel -= 0.01
            if userInput[pygame.K_SPACE]:
                jump = False
                jump = True
            if vel < -1.5:
                jump = False
                vel = 2
        
        if jump == False:
            player.y += vel
        
        if turn == False:
            player.x += turnVel
        
        if player.x > 736:
            turnVel *= -1
            playerImg = playerLImg
            dedplayerImg = dedPlayerLImg
        
        if player.x < 0:
            turnVel *= -1
            playerImg = playerRImg
            dedplayerImg = dedPlayerRImg
        
        if player.y > 536 and ded == False:
            vel = 1
            turn = True
            jump = True
            ded = True
        
        if player.y < 0 and ded == False:
            vel = 1
            turn = True
            jump = True
            ded = True
        
        if ded == True and player.y > 600:
            with open("Assets\DataFiles\Highscore", "w") as highscoreFile:
                json.dump(highscore,highscoreFile)
            running = False
        
        if score > highscore:
            highscore = score
        
        if player.colliderect(CB1) and ded == False:
            score += 1
            CB1skin = random.randint(1,3)
            if CB1skin == 1:
                CB1Img = CB1imagR
            if CB1skin == 2:
                CB1Img = CB1imagL
            if CB1skin == 3:
                CB1Img = CB1imagD
            CB1x = random.randint(0,736)
            CB1y = random.randint(0,536)
            CB1.x = CB1x
            CB1.y = CB1y
        if player.colliderect(CB2) and ded == False:
            score += 1
            CB2skin = random.randint(1,3)
            if CB2skin == 1:
                CB2Img = CB2imagR
            if CB2skin == 2:
                CB2Img = CB2imagL
            if CB2skin == 3:
                CB2Img = CB2imagD
            CB2x = random.randint(0,736)
            CB2y = random.randint(0,536)
            CB2.x = CB2x
            CB2.y = CB2y
        if player.colliderect(CB3) and ded == False:
            score += 1
            CB3skin = random.randint(1,3)
            if CB3skin == 1:
                CB3Img = CB3imagR
            if CB3skin == 2:
                CB3Img = CB3imagL
            if CB3skin == 3:
                CB3Img = CB3imagD
            CB3x = random.randint(0,736)
            CB3y = random.randint(0,536)
            CB3.x = CB3x
            CB3.y = CB3y
        if player.colliderect(SCB1) and ded == False:
            score += 1
            SCB1skin = random.randint(1,3)
            if SCB1skin == 1:
                SCB1Img = SCB1imagR
            if SCB1skin == 2:
                SCB1Img = SCB1imagL
            if SCB1skin == 3:
                SCB1Img = SCB1imagU
            SCB1x = random.randint(0,736)
            SCB1y = random.randint(0,536)
            SCB1.x = SCB1x
            SCB1.y = SCB1y
        if player.colliderect(SCB2) and ded == False:
            score += 1
            SCB2skin = random.randint(1,3)
            if SCB2skin == 1:
                SCB2Img = SCB2imagR
            if SCB2skin == 2:
                SCB2Img = SCB2imagL
            if SCB2skin == 3:
                SCB2Img = SCB2imagU
            SCB2x = random.randint(0,736)
            SCB2y = random.randint(0,536)
            SCB2.x = SCB2x
            SCB2.y = SCB2y
        if player.colliderect(SCB3) and ded == False:
            score += 1
            SCB3skin = random.randint(1,3)
            if SCB3skin == 1:
                SCB3Img = SCB3imagR
            if SCB3skin == 2:
                SCB3Img = SCB3imagL
            if SCB3skin == 3:
                SCB3Img = SCB3imagU
            SCB3x = random.randint(0,736)
            SCB3y = random.randint(0,536)
            SCB3.x = SCB3x
            SCB3.y = SCB3y
        
        screen.blit(CB1Img, CB1)
        screen.blit(CB2Img, CB2)
        screen.blit(CB3Img, CB3)
        screen.blit(SCB1Img, SCB1)
        screen.blit(SCB2Img, SCB2)
        screen.blit(SCB3Img, SCB3)
        
        if ded == False:
            screen.blit(playerImg, player)
        
        if ded == True:
            screen.blit(dedplayerImg, player)
        
        Score()
        high_score()

        pygame.time.delay(3)
        pygame.display.update()
    dedScreen = True
    while dedScreen:

        screen.fill((30,155,227))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                with open("Assets\DataFiles\Highscore", "w") as highscoreFile:
                    json.dump(highscore,highscoreFile)
                pygame.quit()
                sys.exit()
    
        if event.type == pygame.MOUSEBUTTONUP:
            main()
        
        dedHighscore()
        dedScore()
        Stats()
        clickTo()

        pygame.display.update()
main()