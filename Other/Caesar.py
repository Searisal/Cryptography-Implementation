import Format_functions


def caesar_encrypt(string, n):
    string = Format_functions.unformat(string)
    new_string = ""
    for char in string:
        if 97 <= ord(char) <= 122:
            starting_val = ord(char)
            newval = starting_val + n
            shifted_val = 97 + ((newval % 97) % 26)
            new_string += chr(shifted_val)
    return Format_functions.format(new_string)


def caesar_decrypt(string, n):
    string = Format_functions.unformat(string)
    new_string = ""
    for char in string:
        starting_val = ord(char)
        newval = starting_val + (26 - n)
        shifted_val = 97 + ((newval % 97) % 26)
        new_string += chr(shifted_val)
    return new_string


def ROT13(string):
    if string.isupper() == True:  # In order to keep with the convention of lowercase = plaintext, uppercase =
        # cyphertext, if the string is upper, it becomes lower, and vice versa after each application.
        return caesar_decrypt(string, 13)
    else:
        return caesar_encrypt(string, 13)


def numeric_cesear(binary):
    if type(binary) != "str":  # check to make sure that the binary is truly a string
        binary = str(binary)
    if Format_functions.check_integer(binary) == False:  # makes sure the string only has numeric elements
        return "Did not recieve valid input"
    new_numeric_string = ""
    for dec in binary:  # replaces each 1 found in the string with a zero, and vice versa. Stops program if it
        # recieves any other number
        if dec == "1":
            new_numeric_string += "0"
        elif dec == "0":
            new_numeric_string += "1"
        else:
            return "Recieved invalid numbers for a binary system"
    return new_numeric_string
