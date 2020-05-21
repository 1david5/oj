# author: David Lozano
# source: HackerRank ( https://www.hackerrank.com )
# problem name: Algorithms: Strings: Strong Password
# problem url: https://www.hackerrank.com/challenges/strong-password/problem
# date: 05/21/2020

def minimumNumber(n, password):
    numbers = "0123456789"
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    special_characters = "!@#$%^&*()-+"
    n, l, u, s, c = False, False, False, False, 4

    for i in password:
        if not n and i in numbers:
            n = True
            c -= 1
        elif not l and i in lower_case:
            l = True
            c -= 1
        elif not u and i in upper_case:
            u = True
            c -= 1
        elif not s and i in special_characters:
            s = True
            c -= 1
    if c + len(password) >= 6:
        return c
    else:
        return 6 - len(password)
