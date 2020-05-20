# author: David Lozano
# source: HackerRank ( https://www.hackerrank.com )
# problem name: Algorithms: Warmup: Birthday Cake Candles
# problem url: https://www.hackerrank.com/challenges/birthday-cake-candles/problem
# date: 05/18/2020

def birthdayCakeCandles(ar):
    highest = max(ar)
    return ar.count(highest)