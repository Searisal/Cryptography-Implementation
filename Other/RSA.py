import random
import time
import math


def check_if_prime(n):
    prime = True
    i = 2
    if 0 < n < 4:
        return True
    elif n <= 0:
        return "Invalid Input"
    while i <= (n // 2):
        if n % i == 0:
            prime = False
        i += 1
    return prime


def generate_prime_number(min_start, max_start, random_seed=time.time()):
    random.seed(random_seed)
    base_number = random.randint(min_start, max_start)
    prime_found = False
    while prime_found == False:
        if check_if_prime(base_number) == False:
            base_number += 1
        else:
            prime_found = True
    return base_number


def euclidian_algorithm(n_1, n_2):
    n_1 = n_1
    n_2 = n_2
    while n_2 > 0:
        r_i = n_1 % n_2
        n_1 = n_2
        n_2 = r_i
    return n_1


def lcm(n1, n2):
    return int((n1 * n2) / euclidian_algorithm(n1, n2))


def lambda_value(p_1, p_2):
    return lcm(p_1 - 1, p_2 - 1)


def check_e_val(e, p_1, p_2):
    valid = True
    l = lambda_value(p_1, p_2)
    #print(l)
    if (e < 1) or (e > l):
        valid = False
        print("Out of Bounds")
    if euclidian_algorithm(l, e) != 1:
        valid = False
        print("Not Coprime")
    return valid


def get_random_e_val(p1, p2, short):
    i = 3
    l = lambda_value(p1, p2)
    valid_list = []
    while i < l:
        if euclidian_algorithm(l, i) == 1:
            valid_list.append(i)
        i += 1
    if short == True:
        randindex = random.randint(0, 10)
    else:
        randindex = random.randint(0, len(valid_list) - 1)
    return valid_list[randindex]


def extended_euclidian_algorithm(e, n):
    willb = False
    p_i0 = 0
    p_i1 = 1
    e_current = e
    n_current = n
    e_computed = 0
    p_computed = 0
    q_computed = 0
    q_minusone = 0
    q_minustwo = 0
    i = 0
    while willb == False:
        e_computed = n_current % e_current
        q_computed = n_current // e_current
        if i > 1:
            p_computed = (p_i0 - (p_i1 * q_minustwo)) % n
            p_i0 = p_i1
            p_i1 = p_computed
        if n_current == q_computed:
            willb = True
        q_minustwo = q_minusone
        q_minusone = q_computed

        n_current = e_current
        e_current = e_computed
        i += 1
    p_computed = (p_i0 - (p_i1 * q_minustwo)) % n
    return p_computed


def modular_exponent(a, b, n):  ## Computes a^b (mod n)
    i = 0
    result = 1
    while i < b:
        individual_mod = a % n
        #if i % 100 == 0:
            #print(i)
        result = result * individual_mod
        i += 1
    return result % n


def generate_keys(relative_size, random_seed=time.time()):
    prime_one = generate_prime_number(round(math.sqrt(relative_size)), round(math.sqrt(relative_size))+2000, random_seed )
    prime_two = generate_prime_number(round(math.sqrt(relative_size)), round(math.sqrt(relative_size)) + 2000, random_seed+5)
    n_val = prime_one * prime_two
    lambda_n = lambda_value(prime_one, prime_two)
    e_val = get_random_e_val(prime_one, prime_two, True)
    d_val = extended_euclidian_algorithm(e_val, lambda_n)
    return [[n_val, e_val], [n_val, d_val]] # first list is the public key, the second list is the private key

def RSA_encrypt(plaintext, public_key):
    return modular_exponent(plaintext, public_key[1], public_key[0])

def RSA_decrypt(plaintext, private_key):
    return modular_exponent(plaintext, private_key[1], private_key[0])


#test_keys = generate_keys(6, 50)
#print(RSA_decrypt(RSA_encrypt(12345, test_keys[0]), test_keys[1]))