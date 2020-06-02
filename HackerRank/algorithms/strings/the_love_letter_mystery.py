# author: David Lozano
# source: HackerRank ( https://www.hackerrank.com )
# problem name: Algorithms: Strings: The Love-Letter Mystery
# problem url: https://www.hackerrank.com/challenges/the-love-letter-mystery/problem
# date: 06/02/2020

def theLoveLetterMystery(s):
    changes = 0
    for i in range(len(s) // 2):
        lead = s[i]
        tail = s[(i + 1) * -1]
        while lead > tail:
            lead = chr(ord(lead) - 1)
            changes +=1
        while lead < tail:
            tail = chr(ord(tail) - 1)
            changes +=1
    return changes

query_number = int(input())
for _ in range(query_number):
    print(theLoveLetterMystery(input().strip()))
