# author: David Lozano
# source: HackerRank ( https://www.hackerrank.com )
# problem name: Algorithms: Strings: Beautiful Binary String
# problem url: https://www.hackerrank.com/challenges/beautiful-binary-string/problem
# date: 05/28/2020

str_lenght = int(input())
str_input = list(input())
changes = 0
for i in range(1,str_lenght - 1):
    if str_input[i - 1] + str_input[i] + str_input[i + 1] == "010":
        changes += 1
        str_input[i + 1] = "1"
print(changes)