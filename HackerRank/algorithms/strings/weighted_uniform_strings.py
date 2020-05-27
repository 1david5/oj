# author: David Lozano
# source: HackerRank ( https://www.hackerrank.com )
# problem name: Algorithms: Strings: Weighted Uniform Strings
# problem url: https://www.hackerrank.com/challenges/weighted-uniform-string/problem
# date: 05/27/2020

def weight(character):
    return ord(character) - 96

input_string = input()
wheights = [weight(input_string[0])]
for i in range(1,len(input_string)):
    if input_string[i] == input_string[i - 1]:
        wheights.append(wheights[-1] + weight(input_string[i]))
    else:
        wheights.append(weight(input_string[i]))
wheights = set(wheights)
        
for query in range(int(input())):
    print("Yes" if int(input()) in wheights else "No")
