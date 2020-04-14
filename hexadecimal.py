# Implements operations on hexadecimal numbers.
# CSC 225, Assignment 1
# Given code, Winter '20
from binary import add

def binary_to_hex(number):
    """
    Convert a 16-bit binary number to hexadecimal.
    TODO: Implement this function.

    :param number: A bitstring representing the number to convert
    :return: A hexadecimal string, the converted number
    """
    hexe = ''
    number = hex(int(number, 2))
    print(number)
    for i in range(len(number)):
        if number[i] == 'x':
            hexe += 'x0'
        else:
            hexe += number[i].upper()
    return hexe

def hex_to_binary(number):
    """
    Convert a hexadecimal number to 16-bit binary.
    TODO: Implement this function.

    :param number: A hexadecimal string, the number to convert
    :return: A bitstring representing the converted number
    """
    binary='0000000000000000'
    for i in range(int(number, 16)):
        binary = add(binary,'0000000000000001')
    return binary



