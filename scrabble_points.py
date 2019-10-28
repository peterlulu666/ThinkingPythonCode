def bag_of_letters(word_dictionary):
    """
    Params: dictionary where ​key​ = letter and ​value​ = frequency of that letter.
    Returns: a list of letters, with each one repeated according to its frequency.
    Example Input: ​{'A':1, 'B':2}​. Expected output:​ ['A', 'B', 'B']
    """
    # Initialize the letters
    letters = ""
    # We would use for loop to traverse the word_dictionary
    for character, frequency in word_dictionary.items():
        letters = letters + character * int(frequency)
    # Initialize the letter_list
    letter_list = []
    # Store string to list of string
    letter_list[:0] = letters
    return letter_list


def get_word_value(word, word_dictionary):
    """
    Params: a word to evaluate (string), and a dictionary where ​key​ = letter and ​value
    = points that letter is worth.
    Returns: the total point value of the word (an int). If any letter in the word does
    not appear in the letter-value mapping, then return 0 points.
    Example Inputs: ​'HI', {'H':4, 'I':1}​. Expected output: ​5
    Example Inputs: ​'HELLO', {'H':4, 'I':1}​. Expected output: ​0
    """
    # Initialize the point
    point = 0
    word = word.upper()
    # When the key does not exist in dictionary returns 0
    for index in range(0, len(word)):
        if word[index] not in word_dictionary.keys():
            return point
    for letter in word_dictionary:
        point = point + int(word_dictionary[letter])
    return point
