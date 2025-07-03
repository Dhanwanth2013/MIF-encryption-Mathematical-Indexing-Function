from random import choice

digits2_choices = ['/', '<', '>', '?', ':']
digits3_choices = ['|', ';', '_', '-', '{']

def separator(string_list):
    result = []
    for num in string_list:
        if len(num) == 2:
            sep = choice(digits2_choices)
            result.append(sep.join(num))  # e.g. "3>4"
        elif len(num) == 3:
            sep = choice(digits3_choices)
            result.append(sep.join(num))  # e.g. "4;0;6"
        else:
            result.append(num)  # leave single-digit or mutated alone
    return result
