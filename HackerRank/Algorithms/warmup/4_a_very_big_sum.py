# author: David Lozano
# source: HackerRank ( https://www.hackerrank.com )
# problem name: Algorithms: Warmup: A Very Big Sum
# problem url: https://www.hackerrank.com/challenges/a-very-big-sum/problem
# date: 06/09/2019

n = int(input())
list1 = input()
list1 = list1.split()
for i in range(n):
    list1[i] = int(list1[i])

def aVeryBigSum(lst):
    sum = 0
    for i in lst:
        sum += i
    return sum

print(aVeryBigSum(list1))