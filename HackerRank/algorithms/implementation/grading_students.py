# author: David Lozano
# source: HackerRank ( https://www.hackerrank.com )
# problem name: Algorithms: Implementation: Grading Students
# problem url: https://www.hackerrank.com/challenges/grading/problem
# date: 06/01/2020

def gradingStudents(grades):
    rounded_grades = []

    for grade in grades:
        mod5 = grade % 5
        if grade < 38 or mod5 < 3:
            rounded_grades.append(grade)
        else:
            rounded_grades.append(grade + (5 - mod5))
    return rounded_grades

grades_count = int(input().strip())
grades = []
for _ in range(grades_count):
    grades_item = int(input().strip())
    grades.append(grades_item)
result = gradingStudents(grades)
print(result)