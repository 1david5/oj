# author: David Lozano
# source: HackerRank ( https://www.hackerrank.com )
# problem name: Algorithms: Implementation: Angry Professor
# problem url: https://www.hackerrank.com/challenges/angry-professor/problem
# date: 06/29/2020

if __name__ == "__main__":
    for _ in range(int(input())):
        student_count, min_needed = [int(i) for i in input().strip().split()]
        print("NO" if len([int(j) for j in input().strip().split() if int(j) <= 0]) >= min_needed else "YES")