# author: David Lozano
# source: HackerRank ( https://www.hackerrank.com )
# problem name: Algorithms: Implementation: Birthday Chocolate
# problem url: https://www.hackerrank.com/challenges/the-birthday-bar/problem
# date: 06/09/2020

def birthday(l, d, m):
    combinations = 0
    while l and len(l) >= m:
        add = sum(l[:m])
        if add == d:
            combinations += 1
        l.remove(l[0])
    return combinations

n = int(input())
chocoalte_bar = list(map(int, input().strip().split()))
bd = input().strip().split()
day = int(bd[0])
month = int(bd[1])

print(birthday(chocoalte_bar, day, month))