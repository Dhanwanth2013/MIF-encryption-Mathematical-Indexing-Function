from string import ascii_lowercase, ascii_uppercase, punctuation, digits
import random as rd

rd.seed(0)

mutation_prob = 0.5
char_set = ascii_lowercase + ascii_uppercase + punctuation + digits

def return_char_list(string_input):
    return [char for char in string_input]

def char_to_num(char_list):
    return [char_set.index(c) if c in char_set else 99 for c in char_list]

def MInt_function(num_list):
    return [x ** 2 for x in num_list]

def Random_int_mutation(num_list):
    return [str(x + rd.randint(1, 50)) for x in num_list]

def Random_char_mutation(num_list):
    mutated_list = []
    for num in num_list:
        new_str = ''
        for char in str(num):  # iterate through each char of stringified number
            if char.isdigit() and rd.random() < mutation_prob:
                new_str += char_set[int(char)]
            else:
                new_str += char
        mutated_list.append(new_str)
    return mutated_list
