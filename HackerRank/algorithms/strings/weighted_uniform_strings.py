# author: David Lozano
# source: HackerRank ( https://www.hackerrank.com )
# problem name: Algorithms: Strings: Weighted Uniform Strings
# problem url: https://www.hackerrank.com/challenges/weighted-uniform-string/problem
# date: 05/27/2020

def weight(character):
    return ord(character) - 96

original_string = input()
wheights = [weight(original_string[0])]
for i in range(1,len(original_string)):
    if original_string[i] == original_string[i - 1]:
        wheights.append(wheights[-1] + weight(original_string[i]))
    else:
        wheights.append(weight(original_string[i]))
wheights = set(wheights)
        
for query in range(int(input())):
    print("Yes" if int(input()) in wheights else "No")
