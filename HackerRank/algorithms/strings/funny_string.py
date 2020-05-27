# author: David Lozano
# source: HackerRank ( https://www.hackerrank.com )
# problem name: Algorithms: Strings: Funny String
# problem url: https://www.hackerrank.com/challenges/funny-string/problem
# date: 05/27/2020

for i in range(int(input())):
    input_str = input()
    for i in range(1, len(input_str)):
        if abs((ord(input_str[i - 1])) - (ord(input_str[i]))) != abs((ord(input_str[-i])) - (ord(input_str[-i - 1]))):
            print("Not Funny")
            break
    else:
        print("Funny")
    
