# author: David Lozano
# source: HackerRank ( https://www.hackerrank.com )
# problem name: Algorithms: Warmup: Mini-Max Sum
# problem url: https://www.hackerrank.com/challenges/mini-max-sum/problem
# date: 05/30/2019

x = [1,3,5,7,9]

def miniMaxSum(arr):
    min = arr[0]
    max = arr[0]
    for n in arr:
        if n > max:
            max = n
        if n < min:
            min = n
    res = [sum(arr) - max, sum(arr) - min]
    print(*res)

miniMaxSum(x)