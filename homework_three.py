def question_1(name: str) -> str:
    """
    returns "Hello my name  is + Name"

    Parameters:
    ----------
    * name: str - any string that is input while running the function

    Returns:
    ----------
    A string that says Hello my name is + Whatever string is the input

    Examples:
    ----------
    >>> question_1("Rasam")
    "Hello my name is Rasam"
    """

    return (f"Hello my name is {name}")



def question_2(name: str) -> str:
    """
    returns "Hello my name is" plus the capitalization of a name

    Parameters:
    ----------
    *name: str - any string that is input while running the function

    Returns:
    ----------
    A string that says Hello my name is + Capitalized version of the input
    string

    Examples:
    ----------
    >>> question_2("rasam")
    "Hello my name is Rasam"
    """
    
    name_capital = name.title()

    return (f"Hello my name is {name_capital}")



def question_3(name: str) -> str:
    """
    returns "My first name is + Name"

    Parameters:
    ----------
    * name: str - any string that is input while running the function

    Returns:
    ----------
    A string that says My first  name is + Whatever string is the input

    Examples:
    ----------
    >>> question_3("Rasam")
    "My first name is Rasam"
    """

    return (f"My first name is {name}")



def question_4(name: str) -> str:
    """
    returns "My first  name is" plus the capitalization of a name

    Parameters:
    ----------
    *name: str - any string that is input while running the function

    Returns:
    ----------
    A string that says My first  name is + Capitalized version of the input
    string

    Examples:
    ----------
    >>> question_4("rasam")
    "My first name is Rasam"
    """
    
    name_capital = name.capitalize()

    return (f"My first name is {name_capital}")



def question_5(first_name: str, last_name: str) -> str:
    """
    returns "Hello my full name is + first name + last name"

    Parameters:
    ----------
    * first_name: str - any string that is input while running the function
    * last_name: str - any string that is input while running the function

    Returns:
    ----------
    A string that says Hello my full  name is + the two strings that is
    input

    Examples:
    ----------
    >>> question_5("Rasam", "Aminzadeh")
    "My full name is Rasam Aminzadeh"
    """
    return (f"My full name is {first_name} {last_name}")



def question_6(first_name: str, last_name: str) -> str:
    """
    returns "Hello my full name is + capitalized first name + last name"

    Parameters:
    ----------
    * first_name: str - any string that is input while running the function
    * last_name: str - any string that is input while running the function

    Returns:
    ----------
    A string that says Hello my full  name is + the two strings that is
    input

    Examples:
    ----------
    >>> question_6("rasam", "aminzadeh")
    "My full name is Rasam Aminzadeh"
    """
    first_capital = first_name.capitalize()
    last_capital = last_name.capitalize()
    
    return (f"My full name is {first_capital} {last_capital}")



def question_7(string: str) -> list:
    """
    returns indices of the string that are lower case

    Parameters:
    ----------
    * string: str - any string that is input while running the function

    Returns:
    ----------
    A list that contains the indices of lower case characters in a string

    Examples:
    ----------
    >>> question_7("rasam")
    [0, 1, 2, 3, 4]
    """
    lower_characters = [x for x, char in enumerate(string) if char.islower()]
                    
    return lower_characters



def question_8(string: str) -> list:
    """
    returns indices of the string that are upper case

    Parameters:
    ----------
    * string: str - any string that is input while running the function

    Returns:
    ----------
    A list that contains the indices of upper case characters in a string

    Examples:
    ----------
    >>> question_8("Rasam")
    [0]
    """
    upper_characters = [x for x, char in enumerate(string) if char.isupper()]
                    
    return upper_characters



def question_9(string: str) -> list:
    """
    returns indices of the string that are whitespace

    Parameters:
    ----------
    * string: str - any string that is input while running the function

    Returns:
    ----------
    A list that contains the indices of white space characters in a string

    Examples:
    ----------
    >>> question_9("rasam aminzadeh")
    [5]
    """
    space_characters = [x for x, char in enumerate(string) if char.isspace()]
                    
    return space_characters



def question_10(string: str) -> int:
    """
    returns the number of distinct words in the string

    Parameters:
    ----------
    * string: str - any string that is input while running the function

    Returns:
    ----------
    an integer that is the number of distinct words in the string that is input

    Examples:
    ----------
    >>> question_10("i i i i i i m m m m")
    2
    """
    
    unique_words = set(string.split(' '))
    
    my_list = list(unique_words)

    count = len(my_list)
    
    return count



def question_11(string: str) -> list:
    """
    returns the number integers in the string

    Parameters:
    ----------
    * string: str - any string that is input while running the function

    Returns:
    ----------
    an list  that has the number integers in the string that is input

    Examples:
    ----------
    >>> question_11("i i i i i 2 i m m m m")
    [2]
    """
    result = [ i for i in string.split() if i.isdigit()]

    return result



def question_12(x: str, y: str) -> str:
    """
    takes two strings and concatenates them

    Parameters:
    ----------
    * x: str - any string that is input while running the function
    * y: str - any string that is input while running the function

    Returns:
    ----------
    a string that is joined word of the two string that is input

    Examples:
    ----------
    >>> question_12("Rasam", "Aminzadeh")
    "Rasam Aminzadeh"
    """

    z = " ".join([x, y])
    return z

def question_13(x: str, y: str) -> str:
    """
    takes two strings and  concatenates while capitalizing them

    Parameters:
    ----------
    * x: str - any string that is input while running the function
    * y: str - any string that is input while running the function

    Returns:
    ----------
    a string that is joined word of the two string that are capitalized

    Examples:
    ----------
    >>> question_13("rasam", "aminzadeh")
    "Rasam Aminzadeh"
    """
    x_capitalized = x.capitalize()
    y_capitalized = y.capitalize()

    z = " ".join([x_capitalized, y_capitalized])
    return z



def question_14(string: str) -> str:
    """
    takes in a string and replaces spaces with _

    Parameters:
    ----------
    * string: str - any string that is input while running the function

    Returns:
    ----------
    a string that has replaced all spaces with _.

    Examples:
    ----------
    >>> question_14("Rasam Aminzadeh")
    "Rasam_Aminzadeh"
    """

    result = string.replace(" ", "_")

    return result



def question_15(my_list: list) -> str:
    """
    takes in a list of strings then returns the longest word

    Parameters:
    ----------
    * my_list: list - any list that is input while running the function

    Returns:
    ----------
    the longest word in a given list

    Examples:
    ----------
    >>> question_15(["sag", "cats", "is"])
    "cats"
    """

    max_length = -1

    for i in my_list:
        if len(i) > max_length:
            max_length = len(i)
            result = i

    return result



def question_16(my_list: list) -> str:
    """
    takes in a list of strings then returns the shortest word

    Parameters:
    ----------
    * my_list: list - any list that is input while running the function

    Returns:
    ----------
    the shortest word in a given list

    Examples:
    ----------
    >>> question_16(["sag", "cat", "is"])
    "is"
    """

    max_length = 99999

    for i in my_list:
        if len(i) < max_length:
            min_length = len(i)
            result = i

    return result



def question_17(my_list: list) -> float:
    """
    takes in a list of strings then returns the average word length

    Parameters:
    ----------
    * my_list: list - any list that is input while running the function

    Returns:
    ----------
    returns a float that is the average word length in a given list

    Examples:
    ----------
    >>> question_17(["sag", "cat", "isss"])
    "3.666666666665"
    """
    
    average_length = 0
    test_list = []
    for i in my_list:
        test_list.append(len(i))

    result = len(test_list)

    if result == 0:
        average_length = 0
    else:
        average_length = float(sum(test_list))/ result

    return average_length
        
        

def question_18(my_list: list) -> float:
    """
    takes in a list of strings then returns the median word length

    Parameters:
    ----------
    * my_list: list - any list that is input while running the function

    Returns:
    ----------
    returns a float that is the median word length in a given list

    Examples:
    ----------
    >>> question_18(["sag", "cat", "isss"])
    "3.0"
    """

    length = len(my_list)

    middle = length // 2

    result = (len(my_list[middle]) + len(my_list[~middle])) / 2

    return result



def question_19(my_list: list) -> list:
    """
    takes in a list of numbers and retruns the even numbers

    Parameters:
    ----------
    * my_list: list - any list that is input while running the function

    Returns:
    ----------
    returns a list that has the even numbers in a given list

    Examples:
    ----------
    >>> question_19([1, 2, 3, 4, 5, 6, 7])
    [2, 4, 6]
    """
    even_numbers = []

    for i in my_list:
        if i % 2 == 0:
            even_numbers.append(i)

    return even_numbers



def question_20(my_list: list) -> list:
    """
    takes in a list of numbers and retruns the odd numbers

    Parameters:
    ----------
    * my_list: list - any list that is input while running the function

    Returns:
    ----------
    returns a list that has the odd numbers in a given list

    Examples:
    ----------
    >>> question_20([1, 2, 3, 4, 5, 6, 7])
    [1, 3, 5, 7]
    """
    odd_numbers = []

    for i in my_list:
        if i % 2 != 0:
            odd_numbers.append(i)

    return odd_numbers



def question_21(my_list: list) -> list:
    """
    takes in a list of numbers and retruns the three largest numbers

    Parameters:
    ----------
    * my_list: list - any list that is input while running the function

    Returns:
    ----------
    returns a list that has the three largest numbers

    Examples:
    ----------
    >>> question_21([1, 2, 3, 4, 5, 6, 7])
    [5, 6, 7]
    """
    my_list.sort()
    
    largest = my_list[-1]
    second_largest = my_list[-2]
    third_largest = my_list[-3]

    largest_three = [largest, second_largest, third_largest]

    return largest_three



def question_22(my_list: list) -> list:
    """
    takes in a list of numbers and retruns the three smallest numbers

    Parameters:
    ----------
    * my_list: list - any list that is input while running the function

    Returns:
    ----------
    returns a list that has the three smallest numbers

    Examples:
    ----------
    >>> question_22([1, 2, 3, 4, 5, 6, 7])
    [1, 2, 3]
    """
    my_list.sort()

    smallest_three = [my_list[0], my_list[1], my_list[2]]

    return smallest_three



def question_23(my_list: list) -> float:
    """
    takes in a list of numbers and retruns the the mean

    Parameters:
    ----------
    * my_list: list - any list that is input while running the function

    Returns:
    ----------
    returns a list that has the mean of a list

    Examples:
    ----------
    >>> question_22([1, 2, 3, 4])
    2.5
    """
    list_mean = sum(my_list) / len(my_list)

    return list_mean



def question_24(my_list: list) -> float:
    """
    takes in a list of numbers and retruns the the mode

    Parameters:
    ----------
    * my_list: list - any list that is input while running the function

    Returns:
    ----------
    returns a list that has the mode of a list

    Examples:
    ----------
    >>> question_24([1, 4, 3, 4])
    4
    """
    mode = max(my_list, key = my_list.count)

    return mode



def question_25(my_list: list) -> float:
    """
    takes in a list of numbers and retruns the list in reverse

    Parameters:
    ----------
    * my_list: list - any list that is input while running the function

    Returns:
    ----------
    returns the list in reverse

    Examples:
    ----------
    >>> question_25([1, 4, 3, 4])
    [4, 3, 4, 1]
    """

    reversed_list = my_list[::-1]

    return reversed_list



def question_26(my_list: list) -> float:
    """
    returns the cumulative sum of the list of numbers

    Parameters:
    ----------
    * my_list: list - any list that is input while running the function

    Returns:
    ----------
    takes in a list of numbers and returns the cumulative sum of the list of
    numbers

    Examples:
    ----------
    >>> question_26([1, 4, 3, 4])
    12
    """

    sum_list = sum(my_list)

    return sum_list



def question_27(my_list: list) -> float:
    """
    returns the difference between each number and the next number

    Parameters:
    ----------
    * my_list: list - any list that is input while running the function

    Returns:
    ----------
    takes in a list of numbers and returns the difference between each number
    and the next number

    Examples:
    ----------
    >>> question_27([1, 4, 3, 4])
    [-3, 1, -1]
    """

    difference_list = []

    for i in range(len( my_list)-1):
        difference_list.append(my_list[i] - my_list[i + 1])

    return difference_list



def question_28(n: int) -> int:
    """
    a recursive function whose base cases are F[0] = 0, F[1] = 1, F[2] = 1
    and who's nth case is F[n-1] + F[n-3]

    Parameters:
    ----------
    * n: int - any int that is input while running the function

    Returns:
    ----------
    takes a n integer and returns an answer by recursively go through
    F[n-1] + F[n-3] where base cases are F[0] = 0, F[1] = 1, and F[2] = 1

    Examples:
    ----------
    >>> question_28(10)
    19
    """
    
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 1
    else:
        return question_28(n - 1) + question_28(n - 3)



def question_29(n: int) -> int:
    """
    a recursive function that solves for a factorial of a number

    Parameters:
    ----------
    * n: int - any int that is input while running the function

    Returns:
    ----------
    takes a n integer and returns an answer by recursively go through
    F[n-1] * F[n-2] * F[n-3] where the base case is F[0] = 1

    Examples:
    ----------
    >>> question_29(10)
    3628800
    """
    
    if n == 0:
        return 1
    else:
        return n * question_29(n - 1)



def question_30(n: int) -> int:
    """
    a recursive function that solves for 2 to the power of a number

    Parameters:
    ----------
    * n: int - any int that is input while running the function

    Returns:
    ----------
    takes a n integer and returns an answer by recursively go through
    2^F[n-1] * 2^F[n-2] * 2^F[n-3]

    Examples:
    ----------
    >>> question_30(3)
    16
    """
    if n == 0:
        return 1
    else:
        return 2 ** question_30(n - 1)
