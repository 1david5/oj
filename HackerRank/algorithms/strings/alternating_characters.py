# author: David Lozano
# source: HackerRank ( https://www.hackerrank.com )
# problem name: Algorithms: Strings: Alternating Characters
# problem url: https://www.hackerrank.com/challenges/alternating-characters/problem
# date: 05/27/2020

for i in range(int(input())):
    input_str = str(input())
    remove = 0
    for j in range(1, len(input_str)):
        if input_str[j] == input_str[j - 1]:
            remove += 1
    print(remove)
