# author: David Lozano
# source: HackerRank ( https://www.hackerrank.com )
# problem name: Algorithms: Implementation: Divisible Sum Pairs
# problem url: https://www.hackerrank.com/challenges/divisible-sum-pairs/problem
# date: 06/10/2020

def divisible_sum_pair(arr_len, factor, arr):
    count = 0
    for i in range(arr_len - 1):
        for j in range(i + 1, arr_len):
            if (arr[i] + arr[j]) % factor == 0:
                count += 1
    return count

n_k = input().strip().split()
arr_len = int(n_k[0])
factor = int(n_k[1])
arr = list(map(int,input().strip().split()))

print(divisible_sum_pair(arr_len, factor, arr))
