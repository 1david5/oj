# author: David Lozano
# source: HackerRank ( https://www.hackerrank.com )
# problem name: Algorithms: Warmup: Diagonal Difference
# problem url: https://www.hackerrank.com/challenges/diagonal-difference/problem
# date: 05/19/2020

def diagonalDifference(arr):
    d1 = 0
    d2 = 0
    for i in range(len(arr[0])):
        d1 += arr[i][i]
        d2 += arr[i][((i + 1) * -1)]
    return abs(d1 - d2)