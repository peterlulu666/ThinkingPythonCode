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
        print("Points in this round: " + str(totalNumber))
        print("Your total is " + str(totalPoints))
        if totalNumber > 20:
            break
        if totalPoints > 20:
            break

    return totalNumber


def main():
    # Initialize total points
    totalPointOne = 0
    totalPointTwo = 0
    currentNumber = 0
    while True:
        # PlayerOne start to play, choose R or H
        print("It is your turn, PlayerOne \n" +
              "R - Roll \n" +
              "H - Hold \n")

        totalPointOne = Pig(currentNumber, totalPointOne) + totalPointOne
        print("You choose hold and your total is " + str(totalPointOne))

        if totalPointOne >= 20:
            print("Player one wins ")
            sys.exit()
        elif totalPointOne < 20:
            print("It is your turn, PlayerTwo \n" +
                  "R - Roll \n" +
                  "H - Hold \n")

            totalPointTwo = Pig(currentNumber, totalPointTwo) + totalPointTwo
            print("You choose hold and your total is " + str(totalPointTwo))

            if totalPointTwo >= 20:
                print("Player two wins ")
                sys.exit()


main()
