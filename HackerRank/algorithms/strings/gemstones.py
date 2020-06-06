# author: David Lozano
# source: HackerRank ( https://www.hackerrank.com )
# problem name: Algorithms: Strings: Gemstones
# problem url: https://www.hackerrank.com/challenges/gem-stones/problem
# date: 06/06/2020

rock_count = int(input())
gemstones = set(input())
for _ in range(rock_count - 1):
    gemstones = gemstones.intersection(set(input()))
print(len(gemstones))
