# author: David Lozano
# source: HackerRank ( https://www.hackerrank.com )
# problem name: Algorithms: Strings: Caesar Cipher
# problem url: https://www.hackerrank.com/challenges/caesar-cipher-1/problem?h_r=next-challenge&h_v=zen
# date: 05/22/2020

#!/bin/python3

def caesarCipher(s, k):
    encrypted_string = ""
    for char in s:
        encrypted_string += encrypt_letter(char, k)
    return encrypted_string

def encrypt_letter(letter, factor):
    ascii_letter = ord(letter)
    encrypted_letter = ascii_letter + factor

    mins = [65, 97]
    maxs = [90, 122]

    for floor, ceiling in zip(mins, maxs):
        is_alpha = floor <= ascii_letter <= ceiling
        if is_alpha:
            if encrypted_letter <= ceiling:
                return chr(encrypted_letter)
            else:
                encrypted_letter = out_of_range_ascii(encrypted_letter, floor, ceiling)
                return chr(encrypted_letter)
    return letter

def out_of_range_ascii(encrypted_char, minimum, maximum):
    minimum -= 1
    ascii_range_length = 26
    module = (encrypted_char - maximum) % ascii_range_length
    print("module", module)
    print("module", module)
    if not module:
        return maximum
    normalized_char = minimum + module
    return normalized_char