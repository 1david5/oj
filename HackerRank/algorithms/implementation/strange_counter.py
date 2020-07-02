# author: David Lozano
# source: HackerRank ( https://www.hackerrank.com )
# problem name: Algorithms: Implementation: Strange Counter
# problem url: https://www.hackerrank.com/challenges/strange-code/problem
# date: 07/01/2020

if __name__ == "__main__":
    time = int(input())
    count = start = 3
    while count < time:
        count += start * 2
        start *= 2
    print(count - time + 1)