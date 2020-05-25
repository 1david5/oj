# author: David Lozano
# source: HackerRank ( https://www.hackerrank.com )
# problem name: Tutorial: 30 Days of Code: Day 6: Let's Review
# problem url: https://www.hackerrank.com/challenges/30-review-loop/problem
# date: 05/25/2020

test_cases_amount = int(input())
words = []

for i in range(test_cases_amount):
    words.append(input())

for word in words:
    even_chars = ""
    odd_chars = ""
    for i in range(len(word)):
        if i % 2 == 0:
            even_chars += word[i]
        else:
            odd_chars += word[i]
    print(f"{even_chars} {odd_chars}")