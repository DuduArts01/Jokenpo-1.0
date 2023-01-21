import pygame
import os
import sys
from button import Button
from loading import Loading

from mecanic1vComputer import Mecanic1vComputer

#initialization pygame
pygame.init()

#dimension screen
width_screen = 854
height_screen = 480

# display caption
screen = pygame.display.set_mode([width_screen, height_screen], pygame.RESIZABLE)

#       Directory
#   MAIN
directory_main = os.path.dirname(__file__)

#   BUTTON
directory_button = os.path.join(directory_main, "sprite/button")

    #Start
sprite_sheet_start_button = pygame.image.load(os.path.join(directory_button, "start/start.png")).convert_alpha()

    #1V1
sprite_sheet_1v1_button = pygame.image.load(os.path.join(directory_button, "1v1/1v1.png")).convert_alpha()
    #1vComputer
sprite_sheet_1vComputer_button = pygame.image.load(os.path.join(directory_button, "1vComputer/1vComputer.png")).convert_alpha()

    #   hands
directory_hands = os.path.join(directory_button, "hands")

    #Stone
sprite_sheet_stone_button = pygame.image.load(os.path.join(directory_hands, "stone.png")).convert_alpha()

    #Paper
sprite_sheet_paper_button = pygame.image.load(os.path.join(directory_hands, "paper.png")).convert_alpha()
    #Scissors
sprite_sheet_scissors_button = pygame.image.load(os.path.join(directory_hands, "scissors.png")).convert_alpha()

    #Continue button
sprite_sheet_continue_button = pygame.image.load(os.path.join(directory_button, "continue/continue.png")).convert_alpha()

    #Back button
sprite_sheet_back_button = pygame.image.load(os.path.join(directory_button, "back/back.png")).convert_alpha()

#   Loading
directory_loading = os.path.join(directory_main, "sprite/loading")

sprite_sheet_loading = pygame.image.load(os.path.join(directory_loading, "loading.png")).convert_alpha()
sprite_sheet_bar_loading = pygame.image.load(os.path.join(directory_loading, "bar_loading.png")).convert_alpha()



#Main loop control
mainLoop = True
mainmenuLoop = True
loadingLoop = False
menugameLoop = False
loadingGameLoop = False
loop1v1 = False
loop1vComputer = False

start_button = Button(sprite_sheet_start_button, (screen.get_width() / 2), screen.get_height() - (screen.get_height() / 5), 32, 13, 32, 13, (screen.get_width() / 5), (screen.get_height() / 5))


while mainLoop:
    while mainmenuLoop:
        screen.fill([255, 255, 255])

        pygame.display.set_caption("JOKENPO (MAIN MENU)")
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                mainmenuLoop = False
                mainLoop = False
            if event.type == pygame.VIDEORESIZE:
                start_button = Button(sprite_sheet_start_button, (screen.get_width() / 2), screen.get_height() - (screen.get_height() / 5), 32, 13, 32, 13, (screen.get_width() / 5), (screen.get_height() / 5))
        
        if start_button.action:
            loadingLoop = True
            mainmenuLoop = False

        start_button.draw(screen)
        
        pygame.display.update()
    
    #loading on screen
    loading = Loading(sprite_sheet_loading, (screen.get_width() / 2), screen.get_height() - (screen.get_height() / 3), 83, 0, 83, 13, (screen.get_width() / 5), (screen.get_height() / 15), 4, 12, True)
    bar_loading = Loading(sprite_sheet_bar_loading, (screen.get_width() / 2), (screen.get_height() / 2), 32, 0, 32, 16, (screen.get_width() / 5), (screen.get_height() / 5), 8, 3, False)
    
    while loadingLoop:
        pygame.display.set_caption("JOKENPO (LOADING)")
        if(loading.exit_loading):
            screen.fill([0, 0, 0])
            loading.draw(screen)
            bar_loading.draw(screen)
        else:
            menugameLoop = True
            loadingLoop = False

        pygame.display.update()
              
    #Button 1v1
    button_1v1 = Button(sprite_sheet_1v1_button, (screen.get_width() / 3), (screen.get_height() / 2), 33, 33, 33, 33, (screen.get_width() / 10), (screen.get_height() / 6))
    button_1vComputer = Button(sprite_sheet_1vComputer_button, screen.get_width() - (screen.get_width() / 3), (screen.get_height() / 2), 39, 33, 39, 33, (screen.get_width() / 10), (screen.get_height() / 6))
    
    
    while menugameLoop:
        pygame.display.set_caption("JOKENPO (MANU GAME)")
        
        screen.fill([255, 255, 78])
        
        if button_1v1.action:
            loadingGameLoop = True 
            loop1v1 = True
            menugameLoop = False

        if button_1vComputer.action:
            loadingGameLoop = True
            loop1vComputer = True
            menugameLoop = False
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                menugameLoop = False
                mainLoop = False
            if event.type == pygame.VIDEORESIZE:
                button_1v1 = Button(sprite_sheet_1v1_button, (screen.get_width() / 3), (screen.get_height() / 2), 33, 33, 33, 33, (screen.get_width() / 10), (screen.get_height() / 6))
                button_1vComputer = Button(sprite_sheet_1vComputer_button, screen.get_width() - (screen.get_width() / 3), (screen.get_height() / 2), 39, 33, 39, 33, (screen.get_width() / 10), (screen.get_height() / 6))
    
        button_1v1.draw(screen)
        button_1vComputer.draw(screen)

        pygame.display.update()


    #Loading Initialization Game
    loading_game = Loading(sprite_sheet_loading, (screen.get_width() / 2), screen.get_height() - (screen.get_height() / 3), 83, 0, 83, 13, (screen.get_width() / 5), (screen.get_height() / 15), 4, 12, True)
    bar_loading_game = Loading(sprite_sheet_bar_loading, (screen.get_width() / 2), (screen.get_height() / 2), 32, 0, 32, 16, (screen.get_width() / 5), (screen.get_height() / 5), 8, 3, False)

    while loadingGameLoop:
        pygame.display.set_caption("JOKENPO (LOADING GAME)")
        if(loading_game.exit_loading):
            screen.fill([0, 0, 0])
            loading_game.draw(screen)
            bar_loading_game.draw(screen)
        else:
            loadingGameLoop = False

        pygame.display.update()
    
    stone_button = Button(sprite_sheet_stone_button, (screen.get_width() / 3), screen.get_height() - (screen.get_height() / 4), 35, 32, 35, 32, (screen.get_width() / 8), (screen.get_height() / 6))
    paper_button = Button(sprite_sheet_paper_button, (screen.get_width() / 2), screen.get_height() - (screen.get_height() / 4), 33, 37, 33, 37, (screen.get_width() / 9), (screen.get_height() / 6))
    scissors_button = Button(sprite_sheet_scissors_button, screen.get_width() - (screen.get_width() / 3), screen.get_height() - (screen.get_height() / 4), 35, 35, 35, 35, (screen.get_width() / 7.5), (screen.get_height() / 6))
    
    # Button Continue and Back
    continue_button = Button(sprite_sheet_continue_button, (screen.get_width() / 2), (screen.get_height() / 4), 55, 15, 55, 15, (screen.get_width() / 5), (screen.get_height() / 7))
    back_button = Button(sprite_sheet_back_button, (screen.get_width() / 2), (screen.get_height() / 2), 27, 15, 27, 15, (screen.get_width() / 8), (screen.get_height() / 8))
    
    
    #key escape(Esc)
    escape = False
    while loop1v1:
        pygame.display.set_caption("JOKENPO (1V1)")
        screen.fill([155, 155, 155])
        
        

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop1v1 = False
                gameLoop = False
                mainLoop = False
            
            if event.type == pygame.VIDEORESIZE:
                #stone
                stone_button = Button(sprite_sheet_stone_button, (screen.get_width() / 3), screen.get_height() - (screen.get_height() / 4), 35, 32, 35, 32, (screen.get_width() / 8), (screen.get_height() / 6))
                
                #paper
                paper_button = Button(sprite_sheet_paper_button, (screen.get_width() / 2), screen.get_height() - (screen.get_height() / 4), 33, 37, 33, 37, (screen.get_width() / 9), (screen.get_height() / 6))
                
                #scissors
                scissors_button = Button(sprite_sheet_scissors_button, screen.get_width() - (screen.get_width() / 4), screen.get_height() - (screen.get_height() / 3), 35, 35, 35, 35, (screen.get_width() / 7.5), (screen.get_height() / 6))
        
                #continue button
                continue_button = Button(sprite_sheet_continue_button, (screen.get_width() / 2), (screen.get_height() / 4), 55, 15, 55, 15, (screen.get_width() / 5), (screen.get_height() / 7))
                
                #back button
                back_button = Button(sprite_sheet_back_button, (screen.get_width() / 2), (screen.get_height() / 2), 27, 15, 27, 15, (screen.get_width() / 8), (screen.get_height() / 8))
                

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE and escape == True:
                    escape = False
                elif event.key == pygame.K_ESCAPE and escape == False:
                    escape = True
        

        stone_button.draw(screen)
        paper_button.draw(screen)
        scissors_button.draw(screen)
        

        if escape:
            continue_button.draw(screen)
            back_button.draw(screen)

            if continue_button.action:
                escape = False
        
            if back_button.action:
                escape = False
                menugameLoop = True
                loop1v1 = False


        pygame.display.update()
    
    #font
    font = pygame.font.SysFont("arial", int(screen.get_width() / 20), True, False)


    #Score
    score_tie = 0
    score_win = 0
    score_lose = 0

    
    #key Escape(Esc)
    escape = False
    while loop1vComputer:
        pygame.display.set_caption("JOKENPO (1VCOMPUTER)")
        screen.fill([204, 30, 4])
        
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop1vComputer = False
                gameLoop = False
                mainLoop = False
            
            if event.type == pygame.VIDEORESIZE:
                #stone
                stone_button = Button(sprite_sheet_stone_button, (screen.get_width() / 3), screen.get_height() - (screen.get_height() / 4), 35, 32, 35, 32, (screen.get_width() / 8), (screen.get_height() / 6))
                
                #paper
                paper_button = Button(sprite_sheet_paper_button, (screen.get_width() / 2), screen.get_height() - (screen.get_height() / 4), 33, 37, 33, 37, (screen.get_width() / 9), (screen.get_height() / 6))
                
                #scissors
                scissors_button = Button(sprite_sheet_scissors_button, screen.get_width() - (screen.get_width() / 3), screen.get_height() - (screen.get_height() / 4), 35, 35, 35, 35, (screen.get_width() / 7.5), (screen.get_height() / 6))

                #continue button
                continue_button = Button(sprite_sheet_continue_button, (screen.get_width() / 2), (screen.get_height() / 4), 55, 15, 55, 15, (screen.get_width() / 5), (screen.get_height() / 7))
                
                #back button
                back_button = Button(sprite_sheet_back_button, (screen.get_width() / 2), (screen.get_height() / 2), 27, 15, 27, 15, (screen.get_width() / 8), (screen.get_height() / 8))
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE and escape == True:
                    escape = False
                elif event.key == pygame.K_ESCAPE and escape == False:
                    escape = True
            
            
        if stone_button.action:
            print("Clicked")
            mecanic1vComputer = Mecanic1vComputer(1)
            if mecanic1vComputer.result == 0:
                score_tie += 1
            elif mecanic1vComputer.result == 1:
                score_win += 1
            elif mecanic1vComputer.result == -1:
                score_lose += 1

        if paper_button.action:
            print("Clicked")
            mecanic1vComputer = Mecanic1vComputer(2)
            if mecanic1vComputer.result == 0:
                score_tie += 1
            elif mecanic1vComputer.result == 1:
                score_win += 1
            elif mecanic1vComputer.result == -1:
                score_lose += 1
   
        if scissors_button.action:
            mecanic1vComputer = Mecanic1vComputer(3)
            print("Clicked")
            if mecanic1vComputer.result == 0:
                score_tie += 1
            elif mecanic1vComputer.result == 1:
                score_win += 1
            elif mecanic1vComputer.result == -1:
                score_lose += 1

        score_tie_show = f"Tie: {score_tie}"
        score_win_show = f"Win: {score_win}"
        score_lose_show = f"Lose: {score_lose}"
                   
        text_format_score_tie = font.render(score_tie_show, True, (255, 255, 255))
        text_format_score_win = font.render(score_win_show, True, (255, 255, 255))
        text_format_score_lose = font.render(score_lose_show, True, (255, 255, 255))

        stone_button.draw(screen)
        paper_button.draw(screen)
        scissors_button.draw(screen)
                
        screen.blit(text_format_score_tie, ((screen.get_width() / 12), (screen.get_height() / 2)))
        screen.blit(text_format_score_win, ((screen.get_width() / 12), (screen.get_height() / 4)))
        screen.blit(text_format_score_lose, ((screen.get_width() / 12), screen.get_height() - (screen.get_height() / 4)))
        
        

        if escape:
            continue_button.draw(screen)
            back_button.draw(screen)
            
            if continue_button.action:
                escape = False
        
            if back_button.action:
                escape = False
                menugameLoop = True
                loop1vComputer = False


        pygame.display.update()


pygame.quit()
sys.exit()

