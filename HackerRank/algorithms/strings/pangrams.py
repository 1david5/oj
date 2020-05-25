# author: David Lozano
# source: HackerRank ( https://www.hackerrank.com )
# problem name: Algorithms: Strings: Pangrams
# problem url: https://www.hackerrank.com/challenges/pangrams/problem
# date: 05/23/2020

alphabet_letters = {char.lower() for char in input("Enter sentence: ") if char != " "}
print("pangram" if len(alphabet_letters) == 26 else "not pangram")
