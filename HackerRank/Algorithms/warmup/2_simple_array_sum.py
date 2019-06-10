# author: David Lozano
# source: HackerRank ( https://www.hackerrank.com )
# problem name: Algorithms: Warmup: Simple Array Sum
# problem url: https://www.hackerrank.com/challenges/simple-array-sum/problem
# date: 05/29/2019

def simpleArraySum(ar):
    #return sum(ar)
    x = 0
    for i in ar:
        x += i
    return x

n = int(input())
inp = input()
array = inp.split()
for i in range(n):
    array[i] = int(array[i])

simpleArraySum(array)