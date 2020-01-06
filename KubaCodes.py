import math


# 1st EXAMPLE
def count_arithmetic_average(list_of_values):
    """Minicode goal: counting arithmetic average from list values
    First adding every value from list. than sum is divided by list length"""
    sum_of_values = 0
    for value in list_of_values:
        sum_of_values += value
    result = sum_of_values / len(list_of_values)
    # result = sum_of_values / range(list_of_values)   WRONG LINE

    return result


# 2nd EXAMPLE
def evens_list(argument):
    """Minicode goal: returning list of even numbers lower than given argument
    Iterate through list, check if current value is even number
    and add even numbers to result list"""
    list_of_even_numbers = []
    for candidate in range(1, argument):
        if candidate % 2 == 0:
            list_of_even_numbers.append(candidate)
            # list_of_even_numbers.remove(candidate)   # WRONG LINE

    return list_of_even_numbers


# 3rd EXAMPLE
def print_word_without_given_letter(word, given_letter):
    """Minicode goal: returning string without given letter
    Iterate through word and check every letter
    Skip letter given by argument and add other letters to result string
    Print result string at the end"""
    result_word = ""
    for letter in word:
        if letter == given_letter:
            result_word += letter

    print(result_word)
    # abs(result_word)   # WRONG LINE


# 4th EXAMPLE
def print_absolute_value(number):
    """Minicode goal: printing absolute value of given number
    Print if number is bigger or equal 0,
    else get absolute value and print it"""
    if number >= 0:
        print(number)
    else:
        result_value = abs(number)
        # result_value = sum(number)   # WRONG LINE
        print(result_value)


# 5th EXAMPLE
def length_of_section(beginning_point, ending_point):
    """Minicode goal: printing length of section in 2-dimensional Gaussian coordinate system
    Firstly get two coordinates from beginning and ending point
    Count square of difference between second and first coordinate of each point
    Add squares and print square root of sum"""
    x_a, x_b = beginning_point  # coordinates of first point
    y_a, y_b = ending_point  # coordinates of second point
    square_difference_a = pow(x_b - x_a, 2)
    square_difference_b = pow(y_b - y_a, 2)
    sum_of_squares = square_difference_a + square_difference_b
    result = math.sqrt(sum_of_squares)
    # result = math.asin(sum_of_squares)   WRONG LINE
    print(result)


# 6th EXAMPLE
def scalar_product(first_vector_len, second_vector_len, angle_between_vectors):
    """Minicode goal: returns scalar product of two vectors
    Multiply length of vector
    Count cosine of angle between two vectors
    At the end return product of length multiplication and cosine"""
    length_product = first_vector_len * second_vector_len
    cosine_of_angle = math.cos(angle_between_vectors)
    # cosine_of_angle = math.atan2(angle_between_vectors)   # WRONG LINE
    result = length_product * cosine_of_angle

    return result


# 7th EXAMPLE
def vector_length(first_vector):
    """Minicode goal: returns vector length
    Sum square square of every coordinate of vector
    Return square root of sum"""
    sum_of_coordinates_squares = 0
    for coordinate in first_vector:
        sum_of_coordinates_squares += pow(coordinate, 2)

    return math.sqrt(sum_of_coordinates_squares)
    # return math.cos(sum_of_coordinates_squares)   # WRONG LINE


# 8th EXAMPLE
def counting_python_words(statement):
    """Minicode goal: count how many times word 'python' appears in statement
    Algorithm iterate through whole statement, checking if 'python' is found
    If found, counter is increased"""
    counter = 0
    for index in range(len(statement) - 1):
        if statement[index:index + 6] == 'python':
            counter += 1

    return counter
    # return 0     WRONG LINE


# 9th EXAMPLE
def return_bigger(num1, num2):
    """Minicode goal: function return bigger of product or sum of two given values
    Count product and sum of two values and return bigger of them"""
    product = num1 * num2
    sum = sum(num1, num2)

    return max(product, sum)
    # return len(product, sum)   WRONG LINE


# 10th EXAMPLE
def fibonacci_loop(num):
    """Minicode goal: return nth Fibonacci number
    If num is equal 0 return 0
    If num is equal 1 or 2 return 1
    If num is bigger than 2 remember two previous values
    and create current value by adding it"""
    if num == 0:
        return 0
    elif num == 1 or num == 2:
        return 1
    elif num > 2:
        current_value = 0
        a = 1  # variable for (n - 1)
        b = 1  # variable for (n - 2)
        # for _ in all(3, num + 1):  WRONG LINE
        for _ in range(3, num + 1):
            current_value = a + b
            a, b = b, current_value

        return current_value


# 11th EXAMPLE
def create_tuple(csv_argument):
    """Minicode goal: return tuple created from comma separated values given as argument
    Split values and create tuple that contains them"""
    split_values = csv_argument.split(",")
    result_tuple = tuple(split_values)
    # result_tuple = dict(split_values)   WRONG LINE

    return result_tuple


# 12th EXAMPLE
def find_lowercase(statement):
    """Minicode goal: check if lowercase letter appear in statement
    Iterate through statement and check every letter"""
    for letter in statement:
        # if letter.isupper():   WRONG LINE
        if letter.islower():
            return True

    return False


# 13th EXAMPLE
def check_divisibility_by_3_and_5(number):
    """Minicode goal: check if 3 and 5 divide given number
    If both divide number return True, else return False"""
    if number % 3 is 0:
        pass
    else:
        return False

    if number % 5 is 0:
        pass
        # assert   WRONG LINE
    else:
        return False

    return True


# 14th EXAMPLE
def char_frequency(word):
    """Minicode goal: count the number of characters in string
    Put every specific letter and number of their appearances in the dictionary"""
    dict_of_letters = {}
    for n in word:
        keys = dict_of_letters.keys()
        # keys = dict_of_letters.items()   WRONG LINE
        if n in keys:
            dict_of_letters[n] += 1
        else:
            dict_of_letters[n] = 1

    return dict_of_letters


# 15th EXAMPLE
def capitalise_krakow(input_list):
    """Minicode goal: capitalise every 'krakow' occurrence in input_list
    Iterate through list and and capitalise every 'krakow' occurrence
    At last return list with corrected words"""
    result_list = []
    for word in input_list:
        if word == 'krakow':
            word = word.capitalize()
            # word = word.lower()   WRONG LINE
        result_list.append(word)

    return result_list


# 16th EXAMPLE
def replace_first_char_by_last(word):
    """Minicode goal: replace every occurrence of first character in word by last character"""
    first_character = word[0]
    last_character = word[len(word) - 1]
    result_word = word.replace(first_character, last_character)
    # result_word = word.startswith(first_character, last_character)  WRONG LINE

    return result_word


# 17th EXAMPLE
def remove_digits_from_list(list_of_strings):
    """Minicode goal: remove every string from list that is digit"""
    for elem in list_of_strings:
        if elem.isdigit():
            list_of_strings.remove(elem)
            # list_of_strings.extend(elem)   WRONG LINE

    return list_of_strings


# 18th EXAMPLE
def lowercase_first_n_chars(word, n):
    """Minicode goal: return word with first n letters lowercase"""
    result_word = ''
    for index in range(len(word)):
        if index < n:
            result_word += word[index].lower()
            # word[index].upper()   WRONG LINE
        else:
            result_word += word[index]

    return result_word


# 19th EXAMPLE
def find_biggest_length_of_word(words_list):
    """Minicode goal: return biggest length of word from list
    Create list with lengths of every word from input list
    Than find maximal value in list of word lengths"""
    word_lengths = []
    for word in words_list:
        word_lengths.append(len(word))
    biggest_length = max(word_lengths)
    # biggest_length = min(word_lengths)  WRONG LINE

    return biggest_length


# 20th EXAMPLE
def compute_greatest_common_divisor(x, y):
    """Minicode goal: find greatest common divisor
    Firstly find smaller from two given numbers
    Then iterate from 1 to smaller value
    If current value divide both given numbers, save it
    Iterate through whole range and return latest founded value"""
    greatest_common_divisor = 0
    smaller = min(x, y)
    # for i in input(1, smaller + 1):   WRONG LINE
    for i in range(1, smaller + 1):
        if (x % i == 0) and (y % i == 0):
            greatest_common_divisor = i

    return greatest_common_divisor


# 21th EXAMPLE
def delete_duplicates(list_with_dups):
    """Minicode goal: delete all duplicates from list
    Use set to put there every unique value
    Skip value that already is in the set"""
    unique_items = set()
    for x in list_with_dups:
        if x not in unique_items:
            unique_items.add(x)
            # unique_items.remove(x)   WRONG LINE

    return unique_items


# 22th EXAMPLE
def reversed_without_a(word):
    """Minicode goal: return reversed word without a letter
    Firstly remove letter a, than iterate through reversed word and create reversed result"""
    word = word.replace('a', '')
    result_word = ''
    # for letter in sorted(word):   WRONG LINE
    for letter in reversed(word):
        result_word += letter

    return result_word


# 23th EXAMPLE
def find_list_in_list(input_list):
    """Minicode goal: check if list contains any list
    Iterate through list and check if any element is list"""
    for elem in input_list:
        # if issubclass(elem, list):   WRONG LINE
        if isinstance(elem, list):
            return True

    return False


# 24th EXAMPLE
def find_gmail_address(list_of_addresses):
    """Minicode goal: find gmail addresses
    Iterate through list and find every address that ends with 'gmail.com'"""
    gmail_addresses = []
    for address in list_of_addresses:
        # if address.startsswith('gmail.com'):   WRONGLINE
        if address.endswith('gmail.com'):
            gmail_addresses.append(address)

    return gmail_addresses


# 25th EXAMPLE
def convert_into_one_integer(list_of_ints):
    """Minicode goal: return one integer combined from integers from list
    Iterate over the list and convert every integer to string and add to one string
    Return combined string of integers as integer"""
    combined_integers = ''
    for integer in list_of_ints:
        combined_integers += str(integer)
    result_int = int(combined_integers)
    # result_int = tuple(combined_integers)  WRONG LINE

    return result_int


# 26th EXAMPLE
def merge_dicts(dict_1, dict_2, dict_3):
    """Minicode goal: merge 3 dicts into one"""
    merged_dict = {}
    for dict in (dict_1, dict_2, dict_3):
        merged_dict.update(dict)
        # merged_dict.clear(dict)   WRONG LINE

    return merged_dict


# 27th EXAMPLE
def highest_sum(list_of_list):
    """Minicode goal: find highest sum of ints in list
    Iterate through lists and save every list sum
    Than find maximal value and return it"""
    list_of_sums = []
    for list in list_of_list:
        sum_of_list = sum(list)
        list_of_sums.append(sum_of_list)
    maximal_value = max(list_of_sums)
    # maximal_value = sum(list_of_sums)   WRONG LINE

    return maximal_value


# 28th EXAMPLE
def compute_least_common_multiple(x, y):
    """Minicode goal: find lowest common multiple
    Firstly find greater from two given values
    Then check if this value is divided by both given numbers
    If not increment it and check till condition will be fulfilled
    If yes return this value"""
    greater = max(x, y)
    while True:
        if greater % x == 0 and greater % y == 0:
            least_common_multiple = greater
            break
        greater += 1
        # greater += 0   WRONG LINE

    return least_common_multiple


# 29th EXAMPLE
def find_dividers(number):
    """Minicode goal: return list of every divider of given number"""
    list_of_dividers = []
    for i in range(number + 1):
        if i == 0:
            pass
        elif number % i == 0:
            list_of_dividers.append(i)
            # list_of_dividers.remove(i)   WRONG LINE

    return list_of_dividers


# 30th EXAMPLE
def print_numbers(number):
    """Minicode goal: print numbers from 0 to given number included"""
    x = 0
    while True:
        if x <= number:
            print(x)
            # compile(x)   WRONG LINE
            x += 1
        else:
            break
