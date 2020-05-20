# author: David Lozano
# source: HackerRank ( https://www.hackerrank.com )
# problem name: Algorithms: Strings: CamelCase
# problem url: https://www.hackerrank.com/challenges/camelcase/problem
# date: 05/18/2020

def camelcase(s):
    c = 1
    for i in s:
        if 64 < ord(i) <91:
            c += 1
    return c