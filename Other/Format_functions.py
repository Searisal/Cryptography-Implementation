test_integer = 541
test_binary = 11011


## Important note - in this system binary is represented using a string or 1 and zero characters.


## Part 0: Lemma Functions

def check_integer(string_value):  # The function checks if a string contains only integers
    if isinstance(string_value, str) == False:  # Checks for valid input
        return "Invalid input Value"
    try:  # Checks if turning the string into an integer value will cause the program to crash. If it does, then the
        # string obviously contains more than integers.
        int(string_value)
        return True
    except:
        ValueError
        return False

def get_max_power(integer):  # This is a function used to find the highest power of two such that it is still smaller
    # Than or equal to the number itself.
    if isinstance(integer, str) == True:  # Checks for a valid input, either from invalid type or unsuitable number
        return "Invalid input value"
    elif (integer <= 0):
        return "Invalid input value"
    m = 0  # This represents the power itself
    mval = 1  # This represnts the value that 2 to the power is equal to
    while mval <= integer:  # This is a loop which checks, for each power of two starting at zero, whether the power
        # value is less or equal to than the number. While it is, the loop runs.
        m += 1
        mval = 2 ** m
    return m - 1  # one is subtracted from the end in order since the loop will produce a number one power greater
    # Than the one expected.


## Part 1: Converting integer numbers to binary, and vice versa


def binary_to_integer(binary):
    if type(binary) != "str":  # checks to make sure binary is represented as string,
        binary = str(binary)
    integer_value = 0  # This represents the end integer value of the binary string,
    for index_value in range(0, len(binary)):  # The index value i represents, for a digit, it is the ith digit
        # starting from zero on the lefthand side.
        exponent_value = (len(binary) - 1) - index_value  # The exponent value represents the index value of a
        # number, but starting from the righthand side.
        if binary[index_value] == "1":
            integer_value += 2 ** exponent_value  # Add 2 to the exponent value to the total if the digit is 1.
        elif binary[index_value] != "0":  # checks to make sure there is only 1's and 0's in the string,
            return "Encountered non binary number"
    return integer_value


def integer_to_binary(integer, format):
    if isinstance(integer, str) == True:  # Checks for valid input type
        return "Invalid input value"
    elif (integer == 0): # Edge case value to keep from crashing
        return 0
    rem = integer
    binary = 0
    n = get_max_power(integer) # This represents the largest binary digit
    for i in range(0, n + 1):  # This loop, going from the largest binary digit to the lowest, continually subtracts
        # the digits' numerical value from what is left of the true number, given that the digit's value is less than
        # said remainder. If this is the case, a one is put in that digits place, and otherwise it is a zero.
        digit = n-i
        if rem - 2 ** digit >= 0:
            binary += 10 ** digit
            rem -= 2 ** digit
    if format == False:
        return str(binary) # Keeps the convention that binary digits are represented using strings
    else: # Allows for the formatting of binary in terms of an 8 - digit system used for ASCII characters
        binary = str(binary)
        complete_binary = "0" * (8 - len(binary)) + binary
        return complete_binary


## Part 2: Converting strings of text into binary, and vice versa

def string_to_binary(string):
    if type(string) != "str": # Checks for corect formatting
        string = str(string)
    binary = ""
    for char in string: #For each character in the string, first ord() is used to get the unicode INTEGER for the char.
        # From here, it is changed to binary. However, since each unicode binary digit is is 8 spaces and leading
        # zeros are truncated with integers, the extra zeroes are added.
        char_binary = integer_to_binary(ord(char), True)
        binary += char_binary
    return binary

def binary_to_string(binary):
    if isinstance(binary, str) == False: # Multiple checks to make sure that the formatting is exact.
        return "Input not string"
    if check_integer(binary) == False:
        return "Includes non-numeric characters"
    for i in binary:
        if i != "0" and i != "1":
            print(i)
            return "Includes non-binary digits"
    if len(binary) % 8 != 0:
        return "Incorrect binary size"
    character_string = ""
    byte_number = len(binary) // 8 # The number of individual characters in the string
    i = 0
    while i < byte_number:
        byte = binary[(8 * i):(8 * (i + 1))] # Gets the exact 8 characters associated with the ith byte
        char = chr(binary_to_integer(byte)) # Usise teh chr() function to convert the integerized binary digits back
        # to their unicode symbols
        character_string += char
        i += 1
    return character_string

## Part 3: Formatting, along with unformatting, ciphertext

def format(ciphertext):
    if type(ciphertext) != "str":  # check to make sure that what's being formatted is an uppercase string
        ciphertext = str(ciphertext)
    ciphertext = ciphertext.upper()
    if len(ciphertext) <= 5:  # ends the program if the string is too short
        return ciphertext
    new_str = ""
    group_list = []
    i = 5
    while i < len(ciphertext):
        group_list.append(ciphertext[(i - 5):i] + " ")  # for each multiple of 5, take the string of
        # characters from five before up until said number, and add to it a space
        i += 5
    group_list.append(ciphertext[(i - 5):])  # make a group out of the last bunch of letters, which do not have a
    # space at the end and are less than five
    for group in group_list:  # Combine all the grouped letters into one final string
        new_str += group
    return new_str


def unformat(ciphertext):
    if type(ciphertext) != "str":  # check to make sure that what's being non formatted is a string
        ciphertext = str(ciphertext)
    nospace_string = ciphertext.replace(" ", "")  # remove spaces, make lower case
    nospace_string = nospace_string.lower()
    if check_integer(ciphertext) == True:  # if the ciphertext is numeric, it returns it as a number, otherwise, if the
        # ciphertext is alphabetical it returns the string
        return int(nospace_string)
    else:
        return nospace_string