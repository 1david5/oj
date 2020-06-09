# author: David Lozano
# source: HackerRank ( https://www.hackerrank.com )
# problem name: Algorithms: Implementation: Breaking the Records
# problem url: https://www.hackerrank.com/challenges/breaking-best-and-worst-records/problem
# date: 06/09/2020

def breaking_records(scores):
    highest, lowest = scores[0], scores[0]
    high_cnt, low_cnt = 0, 0
    for score in scores:
        if score > highest:
            highest = score
            high_cnt += 1
        elif score < lowest:
            lowest = score
            low_cnt += 1
    return f"{high_cnt} {low_cnt}"

n_games = int(input())
scores_lst = list(map(int, input().strip().split()))

print(breaking_records(scores_lst))