import math


# 1st EXAMPLE
def count_arithmetic_average(list_of_values):
    """Minicode goal: counting arithmetic average from list values"""
    sum_of_values = 0  # sum needed to count average
    for value in list_of_values:
        # adding every value from list
        sum_of_values += value

    # returning sum of values divided by length od list
    return sum_of_values / len(list_of_values)
    # return sum_of_values / range(list_of_values)  # WRONG LINE


# 2nd EXAMPLE
def evens_list(argument):
    """Minicode goal: returning list of evens lower than given argument"""
    list_of_evens = []  # list containing evens
    # for candidate in iter(1, argument):   # WRONG LINE
    for candidate in range(1, argument):
        # checking if candidate is even
        if candidate % 2 == 0:
            # adding value to list
            list_of_evens.append(candidate)
            # list_of_evens.remove(candidate)   # WRONG LINE

    # returning results list
    return list_of_evens


# 3rd EXAMPLE
def print_word_without_given_letter(word, given_letter):
    """Minicode goal: returning string without given letter"""
    result_word = ""  # string variable needed to keep result
    for letter in word:
        # checking if letter should be skipped or added to result
        if letter == given_letter:
            # adding letter to result
            result_word += letter

    # printing result word
    print(result_word)
    # abs(result_word)   # WRONG LINE


# 4th EXAMPLE
def print_absolute_value(number):
    """Minicode goal: printing absolute value of given number"""
    # checking if number is bigger than zero
    if number >= 0:
        # printing result
        print(number)
    else:
        # getting absolute value of number
        result_value = abs(number)
        # result_value = sum(number)   # WRONG LINE
        # printing result
        print(result_value)


# 5th EXAMPLE
def length_of_section(beginning_point, ending_point):
    """Minicode goal: printing length of section"""
    x_a, x_b = beginning_point  # coordinates of first point
    y_a, y_b = ending_point  # coordinates of second point
    # counting square of differences of each point
    square_difference_a = pow(x_b - x_a, 2)
    square_difference_b = pow(y_b - y_a, 2)
    # counting square root of sum square_difference_a and square_difference_b
    print(math.sqrt(square_difference_a + square_difference_b))
    # print(math.asin(square_difference_a + square_difference_b))   # WRONG LINE


# 6th EXAMPLE
def scalar_product(first_vector_len, second_vector_len, angle_between_vectors):
    """Minicode goal: returns scalar product of two vectors"""
    # multiplication of vectors' length
    length_product = first_vector_len * second_vector_len
    # counting cosine of angle between vectors
    cosine_of_angle = math.cos(angle_between_vectors)
    # cosine_of_angle = math.ceil(angle_between_vectors)   # WRONG LINE
    return length_product * cosine_of_angle


# 7th EXAMPLE
def vector_length(first_vector):
    """Minicode goal: returns vector length"""
    sum_of_coordinates_squares = 0
    for coordinate in first_vector:
        # adding squares to sum
        sum_of_coordinates_squares += pow(coordinate, 2)
    # returning square root of sum of squares
    return math.sqrt(sum_of_coordinates_squares)
    # return math.atan(sum_of_coordinates_squares)   # WRONG LINE
