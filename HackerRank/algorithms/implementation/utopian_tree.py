# author: David Lozano
# source: HackerRank ( https://www.hackerrank.com )
# problem name: Algorithms: Implementation: Utopian Tree
# problem url: https://www.hackerrank.com/challenges/utopian-tree/problem
# date: 06/26/2020

for tuple in range(int(input())):
    n = int(input())
    size = 1
    for i in range(1, n + 1):
        if i % 2 == 0:
            size += 1
        else:
            size *= 2
    print(size)