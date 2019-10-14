A = 1
B = 2
C = 3
D = 4
totalScore = 0
character = ""


def QuizScore(choice):
    global totalScore
    if choice == 'A' or choice == 'a':
        totalScore += A
    elif choice == 'B' or choice == 'b':
        totalScore += B
    elif choice == 'C' or choice == 'c':
        totalScore += C
    elif choice == 'D' or choice == 'd':
        totalScore += D


def QuestionOneDisplay():
    print("You're in a burning building with a friend and " +
          "have 10 seconds to get out. " +
          "What do you do? \n")

    print("A - Save myself, of course! \n" +
          "B - Stay and save my friend. \n" +
          "C - If I can save my friend I'll try but if they're going to die anyway, what's the point? \n" +
          "D - Save my friend and everyone else I can find. \n")


def QuestionTwoDisplay():
    print("You're in a burning building with a friend and " +
          "have 10 seconds to get out. " +
          "What do you do? \n")

    print("A - Save myself, of course! \n" +
          "B - Stay and save my friend. \n" +
          "C - If I can save my friend I'll try but if they're going to die anyway, what's the point? \n" +
          "D - Save my friend and everyone else I can find. \n")


def QuestionThreeDisplay():
    print("You're in a burning building with a friend and " +
          "have 10 seconds to get out. " +
          "What do you do? \n")

    print("A - Save myself, of course! \n" +
          "B - Stay and save my friend. \n" +
          "C - If I can save my friend I'll try but if they're going to die anyway, what's the point? \n" +
          "D - Save my friend and everyone else I can find. \n")


def YourCharacter():
    global character
    global totalScore
    if totalScore < 5:
        character = "Slytherin!!!"
    elif totalScore < 8:
        character = "Gryffindor!!!"
    elif totalScore < 11:
        character = "Ravenclaw!!!"
    elif totalScore < 13:
        character = "Hufflepuff!!!"


def Report():
    global totalScore
    global character
    print("You scored " + str(totalScore) +
          " on the quiz, that means you are..." +
          character)


def main():
    QuestionOneDisplay()
    questionOne = input("Enter your selection now \n")
    QuizScore(questionOne)

    QuestionTwoDisplay()
    questionTwo = input("Enter your selection now \n")
    QuizScore(questionTwo)

    QuestionThreeDisplay()
    questionThree = input("Enter your selection now \n")
    QuizScore(questionThree)

    YourCharacter()

    Report()


main()
