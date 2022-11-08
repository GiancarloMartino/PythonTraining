"""
a function is a piece of code that is invoked when you want
"""


def sum_two_number():
    a = 15
    b = 20
    print(a + b)


sum_two_number()


def addition_from_external_inputs():
    first_addend = int(input("Enter a number, please: "))
    second_addend = int(input("Enter a number, please: "))
    print(first_addend + second_addend)


addition_from_external_inputs()
