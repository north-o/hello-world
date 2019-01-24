# A game with stats
import random

Wins = 0
Losses = 0
counter = 0
maxrange = 150



for counter in range(maxrange):

    Game = random.randint(1, 100)
    print (Game)

    if Game > 50:
        print("You won! :) ")
        Wins = Wins+1
    else:
        print("Better luck next time... ):")
        Losses = Losses+1

    Score = Wins-Losses
    Gamesplayed = Wins+Losses
    WinningPercentage = Wins/Gamesplayed

    print ("You have", Wins, "Wins")
    print ("You have", Losses, "Loses")
    print ("Your score is", Score)
    print ("You have played", Gamesplayed, "Games.")
    print ("WinningPercentage is", WinningPercentage)

    Again = input("Do you want to play again? Y/N")
    if Again == "N":
        break