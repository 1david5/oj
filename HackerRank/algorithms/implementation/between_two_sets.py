# author: David Lozano
# source: HackerRank ( https://www.hackerrank.com )
# problem name: Algorithms: Implementation: Between Two Sets
# problem url: https://www.hackerrank.com/challenges/between-two-sets/problem
# date: 06/07/2020

def are_factors(iterable, number):
    for factor in iterable:
        if number % factor != 0:
            return False
    else:
        return True

def are_multipes(iterable, number):
    for multiple in iterable:
        if multiple % number != 0:
            return False
    else:
        return True

def total_between_two_sets(factors, multiples):
    max_factor = max(factors)
    min_multiple = min(multiples)
    valid_number = 0

    for number in range(max_factor, min_multiple + 1):
        if are_factors(factors, number) and are_multipes(multiples, number):
            valid_number += 1
    return valid_number

elements = input().split()
factors = list(map(int,input().strip().split()))
multiples = list(map(int,input().strip().split()))

print(total_between_two_sets(factors, multiples))