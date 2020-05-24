# author: David Lozano
# source: HackerRank ( https://www.hackerrank.com )
# problem name: Algorithms: Strings: Mars Exploration
# problem url: https://www.hackerrank.com/challenges/mars-exploration/problem
# date: 05/23/2020

#!/bin/python3

def marsExploration(s):
    altered = 0
    for i in range(0, len(s), 3):
        if s[i] != "S":
            altered += 1
        if s[i + 1] != "O":
            altered += 1
        if s[i + 2] != "S":
            altered += 1
    return altered
