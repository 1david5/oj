# author: David Lozano
# source: HackerRank ( https://www.hackerrank.com )
# problem name: Algorithms: Strings: Gemstones
# problem url: https://www.hackerrank.com/challenges/gem-stones/problem
# date: 06/06/2020

def gemstones(rocks):
    minerals = set()
    gemsones = 0
    rock_count = len(rocks)
    for rock in rocks:
        minerals.update(set(rock))
    for mineral in minerals:
        counter = 0
        for rock in rocks:
            if mineral in rock:
                counter += 1
                continue
        if counter ==rock_count:
            gemsones += 1
    return gemsones

if __name__ == '__main__':

    n = int(input())

    arr = []

    for _ in range(n):
        arr_item = input()
        arr.append(arr_item)

    print(gemstones(arr))
