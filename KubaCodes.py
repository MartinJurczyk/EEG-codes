import math


# 1st EXAMPLE
def count_arithmetic_average(list_of_values):
    """Funkcja liczy średnią arytmetyczną wartości w liście.
    Przykłady:
    assert count_arithmetic_average([1, 2, 3]) == 2
    assert count_arithmetic_average([4, 4, 16]) == 8"""
    sum_of_values = 0
    for value in list_of_values:
        sum_of_values += value
    result = sum_of_values / len(list_of_values)
    # result = sum_of_values / range(list_of_values)   WRONG LINE

    return result


assert count_arithmetic_average([1, 2, 3]) == 2
assert count_arithmetic_average([4, 4, 16]) == 8


# 2nd EXAMPLE
def even_numbers_list(argument):
    """Funkcja zwraca listę parzystych liczb, które są mniejsze niż podany argument
    Przykłady:
    assert even_numbers_list(8) == [2, 4, 6]
    assert even_numbers_list(5) == [2, 4]"""
    list_of_even_numbers = []
    for candidate in range(1, argument):
        if candidate % 2 == 0:
            list_of_even_numbers.append(candidate)
            # list_of_even_numbers.remove(candidate)   # WRONG LINE

    return list_of_even_numbers


assert even_numbers_list(8) == [2, 4, 6]
assert even_numbers_list(5) == [2, 4]


# 3rd EXAMPLE
def word_without_given_letter(word, given_letter):
    """Funkcja usuwa podaną literę('given_letter') z podanego słowa('word') i zwraca je.
    Przykłądy:
    assert word_without_given_letter('aparat', 'a') == 'prt'
    assert word_without_given_letter('katastrofa', 't') == 'kaasrofa'"""
    result_word = ""
    for letter in word:
        if letter != given_letter:
            result_word += letter

    return result_word
    # abs(result_word)   # WRONG LINE


assert word_without_given_letter('aparat', 'a') == 'prt'
assert word_without_given_letter('katastrofa', 't') == 'kaasrofa'


# 4th EXAMPLE
def absolute_value(number):
    """Funkcja zwraca podaną liczbę jeśli jest większa od 0
    oraz wartość bezwzględną z niej jeśli jest mniejsza od 0.
    Przykłady:
    assert absolute_value(14) == 14
    assert absolute_value(-5) == 5"""
    if number >= 0:
        return number
    else:
        result_value = abs(number)
        # result_value = sum(number)   # WRONG LINE
        return result_value


assert absolute_value(14) == 14
assert absolute_value(-5) == 5


# 5th EXAMPLE
def length_of_section(beginning_point, ending_point):
    """Funkcja zwraca długość odcinka w dwuwymiarowym układzie kartezjańskim.
    Najpierw z obu punktów, które są tuple'ami pobiera pierwszą i drugą współrzędną.
    Następnie oblicza kwadrat różnicy pierwszych i drugich współrzędnych z obu punktów.
    Oba kwadraty dodaje do siebie i zwraca ich pierwiastek kwadratowy.
    Przykłady:
    assert length_of_section((1, 2), (4, 2)) == 3
    assert length_of_section((3, 3), (3, 11)) == 8"""
    x_a, x_b = beginning_point  # współrzędne pierwszego punktu
    y_a, y_b = ending_point  # współrzędne drugiego punktu
    square_difference_a = pow(y_a - x_a, 2)
    square_difference_b = pow(y_b - x_b, 2)
    sum_of_squares = square_difference_a + square_difference_b
    result = math.sqrt(sum_of_squares)
    # result = math.asin(sum_of_squares)   WRONG LINE
    return result


assert length_of_section((1, 2), (4, 2)) == 3
assert length_of_section((3, 3), (3, 11)) == 8


# 6th EXAMPLE
def scalar_product(first_vector_len, second_vector_len, angle_between_vectors):
    """Funkcja zwraca iloczyn skalarny dwóch wektorów.
    Najpierw mnoży długości wektorów, które są podane jako argumenty.
    Następnie oblicza wartość cosinusa kąta pomiędzy wektorami(kąt podany jako argument w radianach).
    Finalnie zawraca wynik mnożenia iloczynu długości razy cosinus kąta.
    Przykłady:
    assert scalar_product(5, 7, math.radians(90)) == 0
    assert scalar_product(5, 5, math.radians(0)) == 25"""
    length_product = first_vector_len * second_vector_len
    cosine_of_angle = math.cos(angle_between_vectors)
    # cosine_of_angle = math.atan2(angle_between_vectors)   # WRONG LINE
    result = length_product * cosine_of_angle

    return result


assert scalar_product(5, 7, math.radians(90)) == 0
assert scalar_product(5, 5, math.radians(0)) == 25


# 7th EXAMPLE
def vector_length(first_vector):
    """Funkcja zwraca długość wektora.
    Najpierw sumuje kwadraty wszystkich współrzędnych wektora,
    a następnie zwraca pierwiastek kwadratowy sumy.
    Przykłady:
    assert vector_length([2, 4, 4]) == 6
    assert vector_length([4, 1, 2, 2]) == 5"""
    sum_of_coordinates_squares = 0
    for coordinate in first_vector:
        sum_of_coordinates_squares += pow(coordinate, 2)

    return math.sqrt(sum_of_coordinates_squares)
    # return math.cos(sum_of_coordinates_squares)   # WRONG LINE


assert vector_length([2, 4, 4]) == 6
assert vector_length([4, 1, 2, 2]) == 5


# 8th EXAMPLE
def counting_python_words(statement):
    """Funkcja liczy ile razy słowo 'python' występuje w podanym wyrażeniu('statement).
    Przykłady:
    assert counting_python_words('python is python') == 2
    assert counting_python_words('no snake') == 0"""
    counter = 0
    for index in range(len(statement) - 1):
        if statement[index:index + 6] == 'python':
            counter += 1

    return counter
    # return False     WRONG LINE


assert counting_python_words('python is python') == 2
assert counting_python_words('no snake') == 0


# 9th EXAMPLE
def return_bigger(num1, num2):
    """Funkcja liczy iloczyn oraz sumę dwóch podanych liczb, a następnie zwraca większe z nich.
    Przykłady:
    assert return_bigger(1, 3) == 4
    assert return_bigger(4, 5) == 20"""
    product = num1 * num2
    suma = num1 + num2

    return max(product, suma)
    # return len(product, sum)   WRONG LINE


assert return_bigger(1, 3) == 4
assert return_bigger(4, 5) == 20


# 10th EXAMPLE
def fibonacci_loop(num):
    """Funkcja liczy n-ty wyraz ciągu Fibonacciego.
    Dla 0 zwraca 0, dla 1 oraz 2 zwraca 1.
    Dla większych liczb niż 2 wylicza kolejne wyrazy dodając do siebie dwa poprzednie,
    aż do momentu znalezienia n-tego wyrazu, który jest zwracany.
    Przykłady:
    assert fibonacci_loop(4) == 3
    assert fibonacci_loop(6) == 8"""
    if num == 0:
        return 0
    elif num == 1 or num == 2:
        return 1
    elif num > 2:
        current_value = 0
        a = 1  # przechowuje wyraz (n - 1)
        b = 1  # przechowuje wyraz (n - 2)
        # for _ in all(3, num + 1):  WRONG LINE
        for _ in range(3, num + 1):
            current_value = a + b
            a, b = b, current_value

        return current_value


assert fibonacci_loop(4) == 3
assert fibonacci_loop(6) == 8


# 11th EXAMPLE
def create_tuple(csv_argument):
    """Zwraca krotkę(tuple) stworzoną z oddzielonych przecinkami wartości w stringu podanych jako argument.
    Najpierw dzieli wartości w miejscu przecinków, a następnie tworzy krotkę i ją zwraca.
    Przykłady:
    assert create_tuple('a,b,c,d') == ('a', 'b', 'c', 'd')
    assert create_tuple('2,4,5') == ('2', '4', '5')"""
    split_values = csv_argument.split(",")
    result_tuple = tuple(split_values)
    # result_tuple = dict(split_values)   WRONG LINE

    return result_tuple


assert create_tuple('a,b,c,d') == ('a', 'b', 'c', 'd')
assert create_tuple('2,4,5') == ('2', '4', '5')


# 12th EXAMPLE
def find_lowercase(statement):
    """Funkcja sprawdza czy w wyrażeniu występuje mała litera.
    Jeśli tak - zwraca True, w przeciwnym przypadku False.
    Przykłady:
    assert find_lowercase('cASaDSFsAAS') == True
    assert find_lowercase('AAA') == False"""
    for letter in statement:
        # if letter.isupper():   WRONG LINE
        if letter.islower():
            return True

    return False


assert find_lowercase('cASaDSFsAAS') == True
assert find_lowercase('AAA') == False


# 13th EXAMPLE
def check_divisibility_by_3_and_5(number):
    """Funkcja sprawdza czy liczba jest podzielna przez 3 i 5.
    Jeśli tak zwraca True, jeśli nie - False.
    Przykłady:
    assert check_divisibility_by_3_and_5(15) == True
    assert check_divisibility_by_3_and_5(9) == False"""
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


assert check_divisibility_by_3_and_5(15) == True
assert check_divisibility_by_3_and_5(9) == False


# 14th EXAMPLE
def char_frequency(word):
    """Funkcja wylicza ilość wystąpień litery w słowie.
    Wyniki umieszczone są w słowniku. Każda litera ma odpowiadającą jej liczbę wystąpień.
    Przykłady:
    assert char_frequency('kaskada') == {'k': 2, 'a': 3, 's': 1, 'd': 1}
    assert char_frequency('anna') == {'a': 2, 'n': 2}"""
    dict_of_letters = {}
    for n in word:
        keys = dict_of_letters.keys()
        # keys = dict_of_letters.items()   WRONG LINE
        if n in keys:
            dict_of_letters[n] += 1
        else:
            dict_of_letters[n] = 1

    return dict_of_letters


assert char_frequency('kaskada') == {'k': 2, 'a': 3, 's': 1, 'd': 1}
assert char_frequency('anna') == {'a': 2, 'n': 2}


# 15th EXAMPLE
def capitalise_krakow(input_list):
    """Funkcja poprawia w każdym wystąpieniu słowa 'krakow' pierwszą literę na wielką.
    Następnie zwraca poprawioną listę.
    Przykłady:
    assert capitalise_krakow(['krakow', 'Jan', 'krak', 'krakow']) == ['Krakow', 'Jan', 'krak', 'Krakow']
    assert capitalise_krakow(['kra', 'kow']) == ['kra', 'kow']"""
    result_list = []
    for word in input_list:
        if word == 'krakow':
            word = word.capitalize()
            # word = word.lower()   WRONG LINE
        result_list.append(word)

    return result_list


assert capitalise_krakow(['krakow', 'Jan', 'krak', 'krakow']) == ['Krakow', 'Jan', 'krak', 'Krakow']
assert capitalise_krakow(['kra', 'kow']) == ['kra', 'kow']


# 16th EXAMPLE
def replace_first_char_by_last(word):
    """Funkcja zamienia każde wystąpienie pierwszej litery w słowie ostatnią literą w słowie.
    Przykłady:
    assert replace_first_char_by_last('aparat') == 'tptrtt'
    assert replace_first_char_by_last('indie') == 'endee'"""
    first_character = word[0]
    last_character = word[len(word) - 1]
    result_word = word.replace(first_character, last_character)
    # result_word = word.startswith(first_character, last_character)  WRONG LINE

    return result_word


assert replace_first_char_by_last('aparat') == 'tptrtt'
assert replace_first_char_by_last('indie') == 'endee'


# 17th EXAMPLE
def remove_digits_from_list(list_of_strings):
    """Funkcja usuwa z listy stringów każdy string który jest cyfrą.
    Następnie zwraca poprawioną listę.
    Przykłady:
    assert remove_digits_from_list(['a', 'd', '4', '5d', '11']) == ['a', 'd', '5d']
    assert remove_digits_from_list(['44' '2', 'd', '14']) == ['d']"""
    for elem in list_of_strings:
        if elem.isdigit():
            list_of_strings.remove(elem)
            # list_of_strings.extend(elem)   WRONG LINE

    return list_of_strings


assert remove_digits_from_list(['a', 'd', '4', '5d', '11']) == ['a', 'd', '5d']
assert remove_digits_from_list(['44' '2', 'd', '14']) == ['d']


# 18th EXAMPLE
def lowercase_first_n_chars(word, n):
    """Funkcja zamienia n pierwszych liter w słowie('word') na małe litery.
     Następnie funkcja zwraca poprawione słowo.
    Przykłady:
    assert lowercase_first_n_chars('ABCDEfghIJ', 4) == 'abcdEfghIJ'
    assert lowercase_first_n_chars('pYTHon', 2) == 'pyTHon'"""
    result_word = ''
    for index in range(len(word)):
        if index < n:
            result_word += word[index].lower()
            # word[index].upper()   WRONG LINE
        else:
            result_word += word[index]

    return result_word


assert lowercase_first_n_chars('ABCDEfghIJ', 4) == 'abcdEfghIJ'
assert lowercase_first_n_chars('pYTHon', 2) == 'pyTHon'


# 19th EXAMPLE
def find_biggest_length_of_word(words_list):
    """Funkcja zwraca długość najdłuższego słowa z podanej listy.
    Najpierw zapisuje długości wszystkich słów do listy,
    a potem szuka w liście wartości maksymalnej.
    Przykłady:
    assert find_biggest_length_of_word(['a', 'aaa', 'aa']) == 3
    assert find_biggest_length_of_word(['ab', 'cds', 'kkkk']) == 4"""
    word_lengths = []
    for word in words_list:
        word_lengths.append(len(word))
    biggest_length = max(word_lengths)
    # biggest_length = min(word_lengths)  WRONG LINE

    return biggest_length


assert find_biggest_length_of_word(['a', 'aaa', 'aa']) == 3
assert find_biggest_length_of_word(['ab', 'cds', 'kkkk']) == 4


# 20th EXAMPLE
def compute_greatest_common_divisor(x, y):
    """Funkcja znajduje największy wspólny dzielnik.
    Najpierw wybiera mniejszą z dwóch podanych liczb.
    Póżniej iteruje od 1 do wybranej liczby.
    Ostatnia znaleziona liczba, która dzieli obie podane liczby jest
    największym wspólnym dzielnikiem.
    Przykłady:
    assert compute_greatest_common_divisor(18, 8) == 2
    assert compute_greatest_common_divisor(21, 14) == 7"""
    greatest_common_divisor = 0
    smaller = min(x, y)
    # for i in input(1, smaller + 1):   WRONG LINE
    for i in range(1, smaller + 1):
        if (x % i == 0) and (y % i == 0):
            greatest_common_divisor = i

    return greatest_common_divisor


assert compute_greatest_common_divisor(18, 8) == 2
assert compute_greatest_common_divisor(21, 14) == 7


# 21th EXAMPLE
def delete_duplicates(list_with_dups):
    """Funkcja usuwa wszystkie duplikaty z podanej listy.
    Każda unikalna wartość jest zapisywana do nowej listy, która jest zwracana.
    Przykłady:
    assert delete_duplicates([1, 2, 3, 3, 2, 5, 6, 7, 7]) == [1, 2, 3, 5, 6, 7]
    assert delete_duplicates([1, 4, 4, 5]) == [1, 4, 5]"""
    unique_items = []
    for x in list_with_dups:
        if x not in unique_items:
            unique_items.append(x)
            # unique_items.remove(x)   WRONG LINE

    return unique_items


assert delete_duplicates([1, 2, 3, 3, 2, 5, 6, 7, 7]) == [1, 2, 3, 5, 6, 7]
assert delete_duplicates([1, 4, 4, 5]) == [1, 4, 5]


# 22th EXAMPLE
def reversed_without_a(word):
    """Funkcja odwraca podane słowo i usuwa z niego litery a.
    Przykłady:
    assert reversed_without_a('Karpaty') == 'ytprK'
    assert reversed_without_a('rosa') == 'sor'"""
    word = word.replace('a', '')
    result_word = ''
    # for letter in sorted(word):   WRONG LINE
    for letter in reversed(word):
        result_word += letter

    return result_word


assert reversed_without_a('Karpaty') == 'ytprK'
assert reversed_without_a('rosa') == 'sor'


# 23th EXAMPLE
def find_list_in_list(input_list):
    """Funkcja sprawdza czy podana lista zawiera w sobie jakąś liste.
    Przykłady:
    assert find_list_in_list([[12, 13], 14, 18]) == True
    assert find_list_in_list(['a', 'abc', 'krk']) == False"""
    for elem in input_list:
        # if enumerate(elem, list):   WRONG LINE
        if isinstance(elem, list):
            return True

    return False


assert find_list_in_list([[12, 13], 14, 18]) == True
assert find_list_in_list(['a', 'abc', 'krk']) == False


# 24th EXAMPLE
def find_gmail_address(list_of_addresses):
    """Funkcja znajduje w podanej liście adresów adresy zakończone na 'gmail.com'.
    Znalezione adresy zostają zwrócone w liście.
    Przykłady:
    assert find_gmail_address(['kuba@o2.pl', 'abcd', 'jakub@gmail.com']) == ['jakub@gmail.com']
    assert find_gmail_address(['kuba@o2.pl', 'abcd']) == []"""
    gmail_addresses = []
    for address in list_of_addresses:
        # if address.startsswith('gmail.com'):   WRONGLINE
        if address.endswith('gmail.com'):
            gmail_addresses.append(address)

    return gmail_addresses


assert find_gmail_address(['kuba@o2.pl', 'abcd', 'jakub@gmail.com']) == ['jakub@gmail.com']
assert find_gmail_address(['kuba@o2.pl', 'abcd']) == []


# 25th EXAMPLE
def convert_into_one_integer(list_of_ints):
    """Funkcja skleja wszystkie liczby z podanej listy liczb w jedną liczbę.
    Liczby z listy są dołączane do siebie jako stringi.
    Wynikowy string zawierający liczbę jest zamieniany na inta i zwracany.
    Przykłady:
    assert convert_into_one_integer([2, 4, 22, 16]) == 242216
    assert convert_into_one_integer([1, 2, 3, 11]) == 12311"""
    combined_integers = ''
    for integer in list_of_ints:
        combined_integers += str(integer)
    result_int = int(combined_integers)
    # result_int = tuple(combined_integers)  WRONG LINE

    return result_int


assert convert_into_one_integer([2, 4, 22, 16]) == 242216
assert convert_into_one_integer([1, 2, 3, 11]) == 12311


# 26th EXAMPLE
def merge_dicts(dict_1, dict_2, dict_3):
    """Funkcja łączy 3 słowniki w jeden i zwraca wynikowy słownik.
    Przykłady:
    assert merge_dicts({'a': 5}, {'b': 1}, {'r': 2}) == {'a': 5, 'b': 1, 'r': 2}
    assert merge_dicts({'a': 5}, {'b': 1, 'c': 3}, {}) == {'a': 5, 'b': 1, 'c': 3}"""
    merged_dict = {}
    for dict in (dict_1, dict_2, dict_3):
        merged_dict.update(dict)
        # merged_dict.clear(dict)   WRONG LINE

    return merged_dict


assert merge_dicts({'a': 5}, {'b': 1}, {'r': 2}) == {'a': 5, 'b': 1, 'r': 2}
assert merge_dicts({'a': 5}, {'b': 1, 'c': 3}, {}) == {'a': 5, 'b': 1, 'c': 3}


# 27th EXAMPLE
def highest_sum(list_of_list):
    """Funkcja znajduje w podanej liście list listę, która ma największą sume elementów.
    Sumy elementów poszczególnych list z listy są przechowywane w dodatkowej liście.
    W dodatkowej liście wyszukiwane jest maximum i zwracane.
    Przykłady:
    assert highest_sum([[1, 2, 3], [5, 4]]) == 9
    assert highest_sum([[1, 1], [6], [2, 3]]) == 6"""
    list_of_sums = []
    for list in list_of_list:
        sum_of_list = sum(list)
        list_of_sums.append(sum_of_list)
    maximal_value = max(list_of_sums)
    # maximal_value = sum(list_of_sums)   WRONG LINE

    return maximal_value


assert highest_sum([[1, 2, 3], [5, 4]]) == 9
assert highest_sum([[1, 1], [6], [2, 3]]) == 6


# 28th EXAMPLE
def compute_least_common_multiple(x, y):
    """Funkcja znajduje najmniejszą wspólną wielokrotność dwóch podanych liczb.
    Najpierw wybiera większą spośród dwóch liczb.
    Następnie zaczynając od wybranej liczby sprawdza czy dzieli obie podane liczby.
    Jeśli nie to inkrementuje liczbę i sprawdza aż do skutku.
    Liczba, która dzieli obie podane liczby jest najmniejszą wspólną wielokrotnością i jest zwracana.
    Przykłady:
    assert compute_least_common_multiple(7, 5) == 35
    assert compute_least_common_multiple(3, 8) == 24"""
    greater = max(x, y)
    while True:
        if greater % x == 0 and greater % y == 0:
            least_common_multiple = greater
            break
        greater += 1
        # greater += 0   WRONG LINE

    return least_common_multiple


assert compute_least_common_multiple(7, 5) == 35
assert compute_least_common_multiple(3, 8) == 24


# 29th EXAMPLE
def find_dividers(number):
    """Funkcja zwraca listę dzielników podanej liczby.
    Funkcja iteruje od 0 aż do podanej liczby i sprawdza każdą liczbę czy jest dzielnikiem.
    Zero jest pomijane.
    Przykłady:
    assert find_dividers(8) == [1, 2, 4, 8]
    assert find_dividers(5) == [1, 5]"""
    list_of_dividers = []
    for i in range(number + 1):
        if i == 0:
            pass
        elif number % i == 0:
            list_of_dividers.append(i)
            # list_of_dividers.remove(i)   WRONG LINE

    return list_of_dividers


assert find_dividers(8) == [1, 2, 4, 8]
assert find_dividers(5) == [1, 5]


# 30th EXAMPLE
def print_numbers(number):
    """Funkcja wypisuje liczby od 0 aż do podanej włącznie."""
    x = 0
    while True:
        if x <= number:
            print(x)
            # compile(x)   WRONG LINE
            x += 1
        else:
            break
