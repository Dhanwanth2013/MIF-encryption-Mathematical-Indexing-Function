from utils import *
from seperator import separator

def encrypt_mif(text):
    # Step 1: Tokenize
    char_list = return_char_list(text)
    
    # Step 2: Convert to numerical face values
    nums = char_to_num(char_list)
    
    # Step 3: Apply MIF logic (e.g. square each number)
    squared = MInt_function(nums)
    
    # Step 4: Add randomness to integers
    mutated = Random_int_mutation(squared)
    
    # Step 5: Random character mutation
    char_mutated = Random_char_mutation(mutated)
    
    # Step 6: Apply randomized separators
    final_encrypted = separator(char_mutated)

    return ''.join(final_encrypted)

# Example
text = input()
print("Encrypted:", encrypt_mif(text))
