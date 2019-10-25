import random
import sys


def Pig(totalNumber, totalPoints):
    while True:
        # PlayerOne enter R or H
        userChoose = input("Enter your choice \n")
        if userChoose == "H" or userChoose == "h":
            break
        # Random number
        number = random.randint(1, 6)
        print("You rolled a " + str(number))
        # Total points in this round
        totalNumber = totalNumber + number
        # Total points in all rounds
        totalPoints = totalPoints + number
        if number == 1:
            totalPoints = totalPoints * 0
            totalNumber = totalNumber * 0
            print("The round is over and you have lost all the points you accumulated in the round")
            print("Points in this round: " + str(totalNumber))
            print("Your total is " + str(totalPoints))
            return number
        print("Points in this round: " + str(totalNumber))
        print("Your total is " + str(totalPoints))
        if totalNumber > 20:
            break
        if totalPoints > 20:
            break
        # If the value on the die is 1,
        # then the round is over and the player has lost all the points they accumulated in the round.

    return totalNumber


def main():
    # Initialize total points
    totalPointOne = 0
    totalPointTwo = 0
    currentNumber = 0
    while True:
        # PlayerOne start to play, choose R or H
        print("PlayerOne start to play, choose R or H \n" +
              "R - Roll \n" +
              "H - Hold \n")

        pigOne = Pig(currentNumber, totalPointOne)
        if pigOne == 1:
            totalPointOne = 0
            print("Round ends. \n")
        else:
            totalPointOne = pigOne + totalPointOne
            print("You choose hold and your total is " + str(totalPointOne))

        if totalPointOne >= 20:
            print("Player one wins ")
            sys.exit()
        elif totalPointOne < 20:
            print("It is your turn, PlayerTwo \n" +
                  "R - Roll \n" +
                  "H - Hold \n")

            pigTwo = Pig(currentNumber, totalPointTwo)
            if pigTwo == 1:
                totalPointTwo = 0
                print("Round ends. \n")
            else:
                totalPointTwo = pigTwo + totalPointTwo
                print("You choose hold and your total is " + str(totalPointTwo))

            if totalPointTwo >= 20:
                print("Player two wins ")
                sys.exit()


main()
