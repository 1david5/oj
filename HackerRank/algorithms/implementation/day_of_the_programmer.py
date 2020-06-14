# author: David Lozano
# source: HackerRank ( https://www.hackerrank.com )
# problem name: Algorithms: Implementation: Day of the Programmer
# problem url: https://www.hackerrank.com/challenges/day-of-the-programmer/problem
# date: 06/12/2020

def day_of_the_programmer(y):
    if y < 1918:
        is_leap_year = y % 4 == 0
        return f"12.09.{y}" if is_leap_year else f"13.09.{y}"
    elif y > 1918:
        is_leap_year = y % 400 == 0 or (y % 4 == 0 and y % 100 != 0)
        return f"12.09.{y}" if is_leap_year else f"13.09.{y}"
    else:
        return "26.09.1918"


year = int(input())
print(day_of_the_programmer(year))