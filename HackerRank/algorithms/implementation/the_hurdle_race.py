# author: David Lozano
# source: HackerRank ( https://www.hackerrank.com )
# problem name: Algorithms: Implementation: The Hurdle Race
# problem url: https://www.hackerrank.com/challenges/the-hurdle-race/problem
# date: 06/25/2020

if __name__ == "__main__":
    hurdle_cnt, max_jump = [int(i) for i in input().strip().split()]
    hurdle_lst = [int(h) for h in input().strip().split()]
    print(max(0, max(hurdle_lst) - max_jump))