# author: David Lozano
# source: HackerRank ( https://www.hackerrank.com )
# problem name: Algorithms: Strings: Pangrams
# problem url: https://www.hackerrank.com/challenges/pangrams/problem
# date: 05/23/2020

print("pangram" if len(set(input().lower() + " ")) >= 27 else "not pangram")