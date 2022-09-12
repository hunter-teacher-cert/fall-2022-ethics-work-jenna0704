# Game of Nim
# Jenna Lin
# CSCI 77800 Fall 2022
# collaborators: 
# consulted:

# imoport random
import random

print ('There are 12 stones in the bag. You and the computer will take turn to remove 1 to 3 stones from the bag. The last person to remove the stones wins the game!')
stones = 12

while stones > 0:
    # prompts user for input
    stonesTaken = int(input('How many stones do you wish to remove? '))
    if stonesTaken > 0 and stonesTaken <= 3:
        
        # calculates the number of stones remaining in the bag, then print
        stones -= stonesTaken
        print('You removed ' + str(stonesTaken) + ' stones. There are ' + str(stones) + ' remaining.')
    
        if stones <= 3:
            print('Computer wins!')
        
        # computer pics a random number between 1-3
        computer = random.choice([1, 2, 3])
        
        # calculates the number of stones remaining in the bag, then print
        stones -= computer
        print('The computer removed ' + str(computer) + ' stones. There are ' + str(stones) + ' stones remanining.')
        
        if stones <= 3:
            print('You win!')
            break
    
    # Shows error message if user inputs a number >3
    else:
        print('You may only remove 1 to 3 stones each time.')
        
        
        

