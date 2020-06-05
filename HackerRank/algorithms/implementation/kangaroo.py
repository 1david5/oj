# author: David Lozano
# source: HackerRank ( https://www.hackerrank.com )
# problem name: Algorithms: Implementation: Kangaroo
# problem url: https://www.hackerrank.com/challenges/kangaroo/problem
# date: 06/04/2020

# Complete the kangaroo function below.
def kangaroo(x1, v1, x2, v2):
    if v2 - v1 == 0:
        return "NO"
    position = (x1 - x2) / (v2 - v1)
    if position > 0 and position % 1 == 0:
        return "YES"
    else:
        return "NO"

if __name__ == '__main__':
    x1V1X2V2 = input().split()

    x1 = int(x1V1X2V2[0])

    v1 = int(x1V1X2V2[1])

    x2 = int(x1V1X2V2[2])

    v2 = int(x1V1X2V2[3])

    result = kangaroo(x1, v1, x2, v2)

    print(result + '\n')

