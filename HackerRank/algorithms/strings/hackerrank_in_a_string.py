# author: David Lozano
# source: HackerRank ( https://www.hackerrank.com )
# problem name: Algorithms: Strings: HackerRank in a String!
# problem url: https://www.hackerrank.com/challenges/hackerrank-in-a-string/problem
# date: 05/26/2020

queries_number = int(input())
queries = []
for i in range(queries_number):
    queries.append(input().lower())

for query in queries:
    filtered_substring = ""
    finder = 0
    for char in query:
        if char == "hackerrank"[finder]:
            filtered_substring += char
            finder += 1
            if len(filtered_substring) == 10:
                break
    print("YES" if filtered_substring == "hackerrank" else "NO")
