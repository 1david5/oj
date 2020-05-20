# author: David Lozano
# source: HackerRank ( https://www.hackerrank.com )
# problem name: Algorithms: Warmup: Staircase
# problem url: https://www.hackerrank.com/challenges/staircase/problem
# date: 05/18/2020

def staircase(n):
    for i in range(n,0,-1):
        m = i - 1
        print(" " * m,"#" * (n-m), sep="")

staircase(10)