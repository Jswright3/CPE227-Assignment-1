# Implements operations on binary numbers.
# CSC 225, Assignment 1
# Given code, Winter '20
# John Wright
from math import pow

def add(addend_a, addend_b):
    """
    Add two 8-bit, two's complement binary numbers; ignore carries/overflows.
    TODO: Implement this function. Do *not* convert the numbers to decimal.

    :param addend_a: A bitstring representing the first number
    :param addend_b: A bitstring representing the second number
    :return: A bitstring representing the sum
    """
    remainder = 0
    new_list = 8 * ['']
    new_str = ''
    for i in range(7, -1, -1):
        if addend_a[i] == '1' and addend_b[i] == '1':
            if remainder == 1:
                new_str = '1' + new_str
            else:
                new_str = '0' + new_str
            remainder = 1
        elif addend_a[i] == '1' or addend_b[i] == '1':
            if remainder == 1:
                new_str = '0' + new_str
                remainder = 1
            else:
                new_str = '1' + new_str
                remainder = 0
        elif addend_a[i] == '0' and addend_b[i] == '0':
            if remainder == 1:
                new_str = '1' + new_str
            else:
                new_str = '0' + new_str
            remainder = 0
    return new_str

def negate(number):
    """
    Negate an 8-bit, two's complement binary number.
    TODO: Implement this function. Do *not* convert the number to decimal.

    :param number: A bitstring representing the number to negate
    :return: A bistring representing the negated number
    """
    inverse = ''
    for i in number:
        if i == '0':
            inverse += '1'
        else:
            inverse += '0'
    return add(inverse, '00000001')

def subtract(minuend, subtrahend):
    """
    Subtract one 8-bit, two's complement binary number from another.
    TODO: Implement this function. Do *not* convert the numbers to decimal.

    :param minuend: A bitstring representing the number from which to subtract
    :param subtrahend: A bitstring representing the number to subtract
    :return: A bitstring representing the difference
    """
    return add(minuend, negate(subtrahend))


def binary_to_decimal(number):
    """
    Convert an 8-bit, two's complement binary number to decimal.
    TODO: Implement this function.

    :param number: A bitstring representing the number to convert
    :return: An integer, the converted number
    """
    decimal = 0
    count = 0
    for i in range(7, 0, -1):
        if number[i] == '1':
            decimal += pow(2, count)
        count += 1
    return decimal

def decimal_to_binary(number):
    """
    Convert a decimal number to 8-bit, two's complement binary.
    TODO: Implement this function.

    :param number: An integer, the number to convert
    :return: A bitstring representing the converted number
    :raise OverflowError: If the number cannot be represented with 8 bits
    """
    binary = '00000000'
    for i in range(number):
        binary = add(binary, '00000001')
        number -= 1
    return binary
