import random
import time
import Format_functions

test_mapping = [57, 89, 74, 36, 65, 125, 113, 66, 73, 121, 34, 61, 42, 39, 124, 52, 38, 43, 59, 37, 91, 118, 101, 76,
                35, 110, 126, 96, 99, 104, 75, 68, 82, 45, 112, 32, 81, 55, 105, 83, 63, 88, 86, 56, 108, 111, 71, 95,
                109, 70, 53, 98, 85, 49, 122, 33, 51, 100, 117, 87, 80, 93, 44, 103, 46, 77, 123, 40, 50, 114, 47, 64,
                84, 60, 94, 62, 115, 41, 107, 92, 120, 54, 106, 116, 119, 69, 90, 58, 67, 78, 102, 79, 97, 72, 48]


test_plaintext = "This is a test"

# Note Important unicode characters range from integers 32 through 126 - ie. 95 individual mappings needed

def check_mapping(mapping):
    if len(mapping) != 95:
        print("Not Correct Size")
        return False
    sorted_list = mapping[:]
    sorted_list.sort()
    for index in range(32,127):
        if (index) != sorted_list[index-32]:
            print("Missing Index " + str(index))
            return False
    return True

def invert_mapping(mapping):
    if check_mapping(mapping)==False:
        return "Incorrect Mapping"
    inverse_mapping = mapping[:]
    index = 0
    for map in mapping:
        inverse_mapping[map-32] = index+32
        index +=1
    return inverse_mapping

def get_random_mapping(random_seed = time.time()):
    mapping = []
    seed_inc = 0
    while len(mapping)<95:
        random.seed(random_seed+seed_inc)
        randnum = random.randint(32, 126)
        seed_inc +=1
        if randnum not in mapping:
            mapping.append(randnum)
    return mapping

def encrypt_substitution(plaintext, mapping):
    if check_mapping(mapping) == False:
        return "Incorrect Mapping"
    if isinstance(plaintext, str) == False:
        return "Incorrect input type"
    ciphertext = ""
    for char in plaintext:
        char_ord = ord(char)
        index = mapping[char_ord-32]
        binary_index = Format_functions.integer_to_binary(index, True)
        new_char = Format_functions.binary_to_string(binary_index)
        ciphertext += new_char
    return ciphertext