import random


# To print the scores of players
def printScores(names, scores, tot_players):
    print("\nPlayer:\t\tPoints:")
    for i in range(0, tot_players):
        print(names[i] + "\t\t" + str(scores[i]))


# main function
def main():
    # getting total number of players
    tot_players = int(input("Enter total players: ")),
    # l ist to store the names of players
    names = []
    # getting the names of all players
    for i in range(0, tot_players):
        names.append(input("Enter the name of player" + str(i + 1) + ": "))
    # l ist to store the score of all players
    scores = []
    # initializing scores of all players to zero
    for i in range(0, tot_players):
        scores.append(0)
    # setting the turn of first player
    turn = 0
    # flag to indicate the game status. setting to false initially
    gameOver = False
    # variable to store user input
    choice = ""
    # variable to store the die value
    roll = 0
    # variable to store the session points of a player score= 0
    # iterating until one player wins
    while not gameOver:
        # calling the function to display scores printScores(names, scores, tot_players)
        # displaying that which player's turn is this print("\nCurrent player: " + names[turn])
        print("Your current round points: " + str(score))
        # getting roll or hold input
        choice = input("Roll/Hold (enter R/H): ")
        # choice for rolling
        if choice == "R" or choice == "r":
            # getting and printing a random number between 1 and 6
            roll = random.randint(1, 6)
            print("\nRolld the die and you got: " + str(roll))
            # random number is 1
            if roll == 1:
                # player lost this session score
                print("You lost this round points:" + str(score))
                # changing the turn to next player
                turn = turn + 1
                if turn == tot_players:
                    turn = 0
                # setting session score to zero for new player
                score = 0
            else:
                # adding random number to round score score+= roll
                if scores[turn] + score >= 20:
                    # current player won the game as he got more than 20 points
                    print("\n" + names[turn] + " got " + str(scores[turn] + score) + " points and won the game")
                    gameOver = True

        elif choice == "H" or choice == "h":
            # adding round points to total score
            scores[turn] += score;
            score = 0
            # choice to hold. giving control to the next player turn = turn + 1
            if turn == tot_players:
                turn = 0
            else:
                # invalid choice
                print("Please enter a valid choice")


# calling the main function
if __name__ == '__main__':
    main()
