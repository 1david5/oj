# author: David Lozano
# source: HackerRank ( https://www.hackerrank.com )
# problem name: Algorithms: Implementation: Sock Merchant
# problem url: https://www.hackerrank.com/challenges/sock-merchant/problem
# date: 06/14/2020

def frequency_list(arr):
    d = {}
    for i in arr:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    return d.values()

def main():
    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    print(sum([freq // 2 for freq in frequency_list(ar)]))

if __name__ == "__main__":
    main()