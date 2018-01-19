# Given a roman numeral, convert it to an integer.

# Input is guaranteed to be within the range from 1 to 3999.


def roman_to_int(roman):
    """LC 13."""
    result = 0
    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    for i in range(len(roman) - 1):  # prevent out of range
        if roman_dict[roman[i]] >= roman_dict[roman[i + 1]]:
            result += roman_dict[roman[i]]
        else:
            result -= roman_dict[roman[i]]
    result += roman_dict[roman[-1]]  # add last value
    return result

