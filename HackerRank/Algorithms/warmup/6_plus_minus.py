# author: David Lozano
# source: HackerRank ( https://www.hackerrank.com )
# problem name: Algorithms: Warmup: Plus Minus
# problem url: https://www.hackerrank.com/challenges/plus-minus/problem
# date: 05/19/2020

def plusMinus(arr):
    lenght = len(arr)
    pos, neg, zero = 0, 0, 0
    for i in arr:
        if i > 0:
            pos += 1
        elif i < 0:
            neg += 1
        else:
            zero += 1
    pos_ration = pos / lenght
    neg_ratio = neg / lenght
    zero_ratio = zero / lenght
    print("{0:.6f}".format(pos_ration))
    print("{0:.6f}".format(neg_ratio))
    print("{0:.6f}".format(zero_ratio))