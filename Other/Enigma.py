import Format_functions
import Simple_substitution
import random
import time


def get_random_plugboard_mapping(switch_number, random_seed = time.time()):
    initial_list = [*range(32,95+32)]
    i = 0
    seed_inc = 0
    while i<switch_number:
        random.seed(random_seed+seed_inc)
        random_number_1 = random.randint(32,94+32)
        random.seed(random_seed + seed_inc+10)
        random_number_2 = random.randint(32,94+32)
        #print(random_number_1, random_number_2)
        if random_number_1 != random_number_2:
            if initial_list[random_number_1-32] == random_number_1 and initial_list[random_number_2-32] == random_number_2:
                i+=1
                initial_list[random_number_1-32] = random_number_2
                initial_list[random_number_2-32] = random_number_1
        seed_inc+=2
    return initial_list

#t = get_random_plugboard_mapping(30)
#print(len(t))

def get_random_reflector_mapping(random_seed = time.time()):
    return "Lol"


def check_reflector_mapping(reflector_mapping):
    return True


def check_plugboard_mapping(plugboard_mapping):
    return True


def reflector(plaintext, reflector_mapping):
    return plaintext


def plugboard(plaintext, plugboard_mapping):
    return plaintext


def shift_rotor_wheel(rotor, turns):
    if Simple_substitution.check_mapping(rotor) == False:
        return "Invalid Mapping"
    turns = turns % len(rotor)
    if turns == len(rotor):
        return rotor
    front_split = rotor[0:turns]
    back_split = rotor[turns:]
    rearranged_list = back_split+front_split
    return rearranged_list


def enigma_encrypt(plaintext, rotor_list, plugboard_mapping, reflector_mapping, rotor_starting_positions):

    ## Part 1: Checking to make sure the arguments are correct
    if isinstance(plaintext, str) == False:
        return "Input is not a string"
    if len(rotor_list) != len(rotor_starting_positions):
        return "Rotor positions do not equal number of rotors"
    i = 1
    while i<=len(rotor_list):
        if Simple_substitution.check_mapping(rotor_list[i-1])==False:
            return "Incorrect Mapping of string #" + str(i)
        i+=1
    if check_plugboard_mapping(plugboard_mapping)==False:
        return "Incorrect plugboard mapping"
    if check_reflector_mapping(reflector_mapping)==False:
        return "Incorrect reflector mapping"

    ## Part 2: Set up the rotors into the correct starting position
    current_rotor_list = rotor_list[:]
    j = 0
    while j<len(rotor_list):
        current_rotor_list[j] = shift_rotor_wheel(rotor_list[j], rotor_starting_positions[j])
        j+=1

    ciphertext = ""
    for char in plaintext:
        ## Part 3: Encipherment & Rotor Shift
        cipher_char = Simple_substitution.encrypt_substitution(char, plugboard_mapping)
        #print("Applied Plugboard - " + cipher_char)
        k = 0
        while k<len(rotor_list):
            cipher_char = Simple_substitution.encrypt_substitution(cipher_char, current_rotor_list[k])
            #print("Applied Rotor "+str(k) + " - "  + cipher_char)
            k+=1
        k -=1
        cipher_char = Simple_substitution.encrypt_substitution(cipher_char, reflector_mapping)
        #print("Applied Reflector - " + cipher_char)
        while k>=0:
            cipher_char = Simple_substitution.encrypt_substitution(cipher_char, Simple_substitution.invert_mapping(current_rotor_list[k]))
            current_rotor_list[k] = shift_rotor_wheel(current_rotor_list[k], 1)
            #print("Applied Inverse Rotor " + str(k) + " - " + cipher_char)
            k -=1
        cipher_char = Simple_substitution.encrypt_substitution(cipher_char, plugboard_mapping)
        #print("Applied Plugboard - " + cipher_char)
        ciphertext += cipher_char
    return ciphertext

"""
Test_Rotor = Simple_substitution.get_random_mapping(1)

Test_Rotors = [Simple_substitution.get_random_mapping(5), Simple_substitution.get_random_mapping(18),
               Simple_substitution.get_random_mapping(9)]

Test_Rotor_starting_Positions = [34, 17, 91]

Test_Plugboard = get_random_plugboard_mapping(30, 122)

Test_Reflector = get_random_plugboard_mapping(47, 67)

T = enigma_encrypt("This is a test to see whether my enigma cipher machine works.", Test_Rotors, Test_Plugboard, Test_Reflector, Test_Rotor_starting_Positions)

#print(Test_Plugboard)
#print(Simple_substitution.invert_mapping(Test_Plugboard))
print(T)
print(enigma_encrypt(T, Test_Rotors, Test_Plugboard, Test_Reflector, Test_Rotor_starting_Positions))
"""
