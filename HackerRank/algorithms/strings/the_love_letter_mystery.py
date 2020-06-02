# author: David Lozano
# source: HackerRank ( https://www.hackerrank.com )
# problem name: Algorithms: Strings: The Love-Letter Mystery
# problem url: https://www.hackerrank.com/challenges/the-love-letter-mystery/problem
# date: 06/02/2020

def theLoveLetterMystery(s):
    changes = 0
    for i in range(len(s) // 2):
        changes += abs(ord(s[i]) - ord(s[-(i + 1)]))
    return changes

query_number = int(input())
for _ in range(query_number):
    print(theLoveLetterMystery(input().strip()))
