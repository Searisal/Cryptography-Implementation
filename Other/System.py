import Format_functions
import Simple_substitution
import Enigma
import RSA

def key_to_positions(key):
    rotor_starting_list = []
    key_str = str(key)
    if len(key_str)%2 == 1:
        key_str = "0"+key_str
    for i in range(0, len(key_str)//2):
        rotor_start = key_str[(2*i):((2*i)+2)]
        rotor_starting_list.append(int(rotor_start))
    return rotor_starting_list

def encrypt_message(plaintext, rotor_list, plugboard_mapping, reflector_mapping, sender_private_key, reciever_public_key, starting_positions):
    encrypted_start_positions = RSA.RSA_encrypt(starting_positions, reciever_public_key)
    authenticated_start_positions = RSA.RSA_encrypt(encrypted_start_positions, sender_private_key)
    main_ciphertext = Enigma.enigma_encrypt(plaintext, rotor_list, plugboard_mapping, reflector_mapping, key_to_positions(starting_positions))
    total_message = [authenticated_start_positions, main_ciphertext]
    return total_message


def decrypt_message(authenticated_start_positions, main_ciphertext, rotor_list, plugboard_mapping, reflector_mapping, sender_public_key, receiver_private_key):
    unauthenticated_start_positions = RSA.RSA_decrypt(authenticated_start_positions, sender_public_key)
    start_positions = RSA.RSA_decrypt(unauthenticated_start_positions, receiver_private_key)
    list_start_positions =key_to_positions(start_positions)
    plaintext = Enigma.enigma_encrypt(main_ciphertext, rotor_list,plugboard_mapping,reflector_mapping,list_start_positions)
    return plaintext

test_message = "Hello World! I think that I have finally completed this project, and I'm fairly certian that this will work well. "
starting_positions = 349651

test_rotors = [Simple_substitution.get_random_mapping(5), Simple_substitution.get_random_mapping(10), Simple_substitution.get_random_mapping(15)]
test_reflector = Enigma.get_random_plugboard_mapping(47, 20)
test_plugboard = Enigma.get_random_plugboard_mapping(30, 25)

test_sender_keys = RSA.generate_keys(6, 30)
test_receiver_keys = RSA.generate_keys(6,35)

test_encrypted_message = encrypt_message(test_message,test_rotors,test_plugboard,test_reflector, test_sender_keys[1], test_receiver_keys[0],starting_positions )
print(test_encrypted_message)
test_decrypted_message = decrypt_message(test_encrypted_message[0], test_encrypted_message[1], test_rotors, test_plugboard, test_reflector, test_sender_keys[0], test_receiver_keys[1])
print(test_decrypted_message)