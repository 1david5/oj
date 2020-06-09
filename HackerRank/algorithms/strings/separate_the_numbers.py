# author: David Lozano
# source: HackerRank ( https://www.hackerrank.com )
# problem name: Algorithms: Strings: Separate the Numbers
# problem url: https://www.hackerrank.com/challenges/separate-the-numbers/problem
# date: 06/09/2020

def it_works(n, s):
    pass
    n = int(n)
    while s and s[:len(str(n))] == str(n):
        s = s[len(str(n)):]
        n += 1
    return s

def separate_numbers(s):
    for i in range(len(s) - 1):
        n = s[:i + 1]
        if it_works(n, s) == "":
            return f"YES {n}"
    return "NO"

if __name__ == '__main__':
    q = int(input())

    for q_itr in range(q):
        s = input()

        print(separate_numbers(s))