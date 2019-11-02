def absolute(number):
    """
    Name​: ​absolute
    Input​: one number (float or int)
    Returns​: a number (float or int), the absolute value of the given input.
    The absolute value of a number is its magnitude without regard for its sign
    """
    if number > 0:
        return number
    else:
        return number * (-1)


def manhattan(x_one, y_one, x_two, y_two):
    """
    Name​: ​manhattan
    Input​: four numbers (ints or floats), representing two coordinates (​x1, y1, x2, y2​)
    Returns​: a float, the manhattan distance between the two coordinates
    """
    distance = absolute(x_two - x_one) + absolute(y_two - y_one)
    return distance


def euclidean(x_one, y_one, x_two, y_two):
    """
    Name​: ​euclidean
    Input​: four numbers (ints or floats), representing two coordinates (​x1, y1, x2, y2​)
    Returns​: a float, the euclidean distance between the two coordinates
    """
    distance = (((x_two - x_one) ** 2) + ((y_one - y_two) ** 2)) ** 0.5
    return distance


