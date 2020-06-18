# author: David Lozano
# source: HackerRank ( https://www.hackerrank.com )
# problem name: Algorithms: Implementation: Cats and a Mouse
# problem url: https://www.hackerrank.com/challenges/cats-and-a-mouse/problem
# date: 06/18/2020

def cat_and_mouse(cat_a, cat_b, m):
    if abs(cat_a - m) < abs(cat_b - m):
        return "Cat A"
    elif abs(cat_a - m) > abs(cat_b - m):
        return "Cat B"
    else:
        return "Mouse C"

def main():
    querie_count = int(input())
    for _ in range(querie_count):
        cat_a, cat_b, mouse = [int(position) for position in input().strip().split()]
        print(cat_and_mouse(cat_a, cat_b, mouse))

if __name__ == "__main__":
    main()