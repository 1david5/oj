# author: David Lozano
# source: HackerRank ( https://www.hackerrank.com )
# problem name: Algorithms: Implementation: Picking Numbers
# problem url: https://www.hackerrank.com/challenges/picking-numbers/problem
# date: 06/20/2020

def picking_numbers(n, arr):
    arr = sorted(arr)
    count = 0
    for i in range(n - 1):
        j = i + 1
        temp = 1
        while j <= n - 1 and abs(arr[i] - arr[j]) <= 1 :
            temp += 1
            j += 1
        if temp > count:
            count = temp
    return count

def main():
    n = int(input())
    arr = [int(i) for i in input().strip().split()]
    print(picking_numbers(n, arr))

if __name__ == "__main__":
    main()