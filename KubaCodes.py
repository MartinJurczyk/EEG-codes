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
    result_word = ""   # string variable needed to keep result
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
