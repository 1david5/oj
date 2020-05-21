# author: David Lozano
# source: HackerRank ( https://www.hackerrank.com )
# problem name: Algorithms: Implementation: Apple and Orange
# problem url: https://www.hackerrank.com/challenges/apple-and-orange/problem
# date: 05/20/2020

def countApplesAndOranges(s, t, a, b, apples, oranges):
    a_min = s - a
    a_max = t - a
    o_min = t - b
    o_max = s - b
    app = 0
    org = 0
    for d in apples:
        if a_min <= d <= a_max:
            app += 1
    for d in oranges:
        if o_max <= d <= o_min:
            org += 1
    print(f"{app}\n{org}")

countApplesAndOranges(7, 11, 5, 15, [-2, 2, 1], [5, -6])