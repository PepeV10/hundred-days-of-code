"""

# DATA TYPES

# String
"Hello"[4]

# Integer
print(123 + 345)

# Float
3.14159

# Boolean
True
False

"""

"""

Instructions

Write a program that adds the digits in a 2 digit number e.g. if the input was 35, then the output should be 3 + 5 = 8
Warning: Do not change the code on line 1. Your program should work for different inputs e.g. any two digit number.

The last line of your program should print the result

Example 1 Input
39

Example 1 Output
12

Example 2 Input
43

Example 2 Output
7
"""

# My Solution
"""
two_digit_number = input()


num_1 = two_digit_number[0]
num_2 = two_digit_number[1]

final_sum = int(num_1) + int(num_2)
print(final_sum)
"""

# Angela's Solution
two_digit_number = input()

first_digit = int(two_digit_number[0])
second_digit = int(two_digit_number[1])

two_digit_number = first_digit + second_digit
print(two_digit_number)
