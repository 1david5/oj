# author: David Lozano
# source: HackerRank ( https://www.hackerrank.com )
# problem name: Algorithms: Implementation: Extra Long Factorials
# problem url: https://www.hackerrank.com/challenges/extra-long-factorials/problem
# date: 06/14/2020

n = f = int(input())

while n > 1:
    f *= n - 1
    n -= 1

print(f)