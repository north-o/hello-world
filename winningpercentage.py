# A game with stats
import random

Game = random.randint(1, 100)
print (Game)

Wins = 0
Loses = 0

if Game > 50:
    print("You won! :) ")
    Wins = Wins+1
else:
    print("Better luck next time... ):")
    Loses = Loses+1

