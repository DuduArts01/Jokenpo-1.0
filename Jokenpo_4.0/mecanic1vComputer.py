import pygame
import random

class Mecanic1vComputer():
    def __init__(self, player):
        computer = random.randint(1, 3)
        
        #Tie
        if player == computer:
            self.result = 0
        
        else:
            #Player Won
            if player == 1 and computer == 3:
                self.result = 1
            elif player == 2 and computer == 1:
                self.result = 1
            elif player == 3 and computer == 2:
                self.result = 1

            #Player Lose
            elif player == 3 and computer == 1:
                self.result = -1
            elif player == 1 and computer == 2:
                self.result = -1
            elif player == 2 and computer == 3:
                self.result = -1
