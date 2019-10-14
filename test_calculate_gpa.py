from calculate_gpa import calculate_gpa

EPSILON = 0.001


def test_calculate_gpa(curr_gpa, num_classes, new_grade, expected):
    """
    Function test_calculate_gpa
    Parameters: gpa (float), # classes (int), new grade (float)
    ...all are inputs to the imported function update_gpa...
    and a float, for the expected output after calling
    the function
    Returns: True if test passed, False if it didn't
    """

    print('Current GPA:', curr_gpa,
          'Num classes:', num_classes,
          'New grade:', new_grade)

    print('Expected output:', expected)

    actual = calculate_gpa(curr_gpa,
                           num_classes,
                           new_grade)

    if abs(actual - expected) < EPSILON:
        print('...SUCCESS!\n')
        return True
    else:
        print('...FAIL :(\n')
        return False


def main():
    num_passed = 0
    num_failed = 0
    if test_calculate_gpa(4.0, 1, 4.0, 4.0):
        num_passed += 1
    else:
        num_failed += 1


main()
