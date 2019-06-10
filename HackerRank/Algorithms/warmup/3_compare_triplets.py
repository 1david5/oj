# author: David Lozano
# source: HackerRank ( https://www.hackerrank.com )
# problem name: Algorithms: Warmup: Compare the Triplets
# problem url: https://www.hackerrank.com/challenges/compare-the-triplets/problem
# date: 05/29/2019


def compareTriplets(a, b):
    ana = 0
    bob = 0
    for n in range(3):
        if a[n]>b[n]:
            ana += 1
        elif a[n]<b[n]:
            bob += 1
    array = [ana,bob]
    return array

input1 = input()
input1 = input1.split()
input2 = input()
input2 = input2.split()
for i in range(3):
    input1[i] = int(input1[i])
    input2[i] = int(input2[i])

print(*compareTriplets(input1,input2))