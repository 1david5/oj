# author: David Lozano
# source: HackerRank ( https://www.hackerrank.com )
# problem name: Algorithms: Implementation: Drawing Book
# problem url: https://www.hackerrank.com/challenges/drawing-book/problem
# date: 06/15/2020

def page_count(page, total):
    if page > total // 2:
        if total % 2 == 0:
            return (total - page + 1) // 2
        else:
            return (total - page) // 2
    else:
        return page // 2

def main():
    total = int(input())
    page = int(input())
    print(page_count(page, total))

if __name__ == "__main__":
    main()