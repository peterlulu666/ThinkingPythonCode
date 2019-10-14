import time

import sentence

import sys


def main():
    # Create the list to store user typing
    phraseList = []

    # The index of the list
    phraseIndex = 0

    # The number of words typed and
    # number of mistakes made should be integers throughout the program
    wordNumber = 0

    mistakes = 0

    print("Welcome to the WPM test! "
          "Type each sentence exactly as it appears \n "
          "Or type DONE and well end the test. \n ")

    # prompt the user to just press Enter at the beginning,
    # and start the timer right after that
    userEnter = input("Hit enter when ready and "
                      "we will start the clock \n")

    # The user might type DONE at the very
    # beginning and just get zeroes for everything
    if userEnter == "DONE":
        print("You typed 0 words in 0 seconds. \n" +
              "Your overall wpm is 0 \n")
        sys.exit(0)

    # Start counting seconds
    typingStart = time.time()

    while True:
        phraseList.append(sentence.select_sentence())
        print(phraseList[phraseIndex])
        userPhrase = input()
        # The test must keep going,
        # selecting sentence after sentence after sentence until
        # the user types DONE
        if userPhrase == "DONE":
            break

        if userPhrase == "":
            wordNumber = wordNumber + 0
        else:
            wordNumber = wordNumber + sentence.count_words(userPhrase)

        mistakes = mistakes + sentence.count_mismatches(phraseList[phraseIndex], userPhrase)
        phraseIndex = phraseIndex + 1

    # You should stop the timer right after they type DONE
    # Stop count seconds
    typingEnd = time.time()

    # Total time in seconds
    totalSeconds = typingEnd - typingStart
    # Total time in minutes
    totalMinutes = totalSeconds / 60

    # The number of seconds should be rounded to the nearest 100th
    print("You typed " + str(wordNumber) + " words" +
          " in " + str(round(totalSeconds, 2)) + " seconds ")

    # he words per minute and adjusted words per minute,
    # when reported on the terminal,
    # should be rounded to the nearest whole number
    print("Your overall wpm is " + str(int(wordNumber / totalMinutes)))

    print("You made " + str(mistakes) + " mistakes, so your adjusted wpm is " +
          str(int((wordNumber - mistakes) / totalMinutes)))


main()
