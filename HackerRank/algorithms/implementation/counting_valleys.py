# author: David Lozano
# source: HackerRank ( https://www.hackerrank.com )
# problem name: Algorithms: Implementation: Counting Valleys
# problem url: https://www.hackerrank.com/challenges/counting-valleys/problem
# date: 06/16/2020

def counting_valleys(s):
    track = 0
    valleys = 0
    for step in s:
        if step == "U":
            track += 1
            if track == 0:
                valleys += 1
        elif step == "D":
            track -= 1
    return valleys

def main():
    n = int(input())
    steps = input().strip()
    print(counting_valleys(steps))

if __name__ == "__main__":
    main()