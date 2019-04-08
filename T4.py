#!/bin/python3

import os
import sys

#
# Complete the gradingStudents function below.
#
def gradingStudents(grades):
    result = []
    i = 0
    while i < len(grades):
        if grades[i] < 38:
            result.append(grades[i])
        elif grades[i] < 40:
            if 40 - grades[i] < 3:
                result.append(40)
            else:
                result.append(grades[i])
        elif grades[i] < 45:
            if 45 - grades[i] < 3:
                result.append(45)
            else:
                result.append(grades[i])
        elif grades[i] < 55:
            if 55 - grades[i] < 3:
                result.append(55)
            else:
                result.append(grades[i])
        elif grades[i] < 60:
            if 60 - grades[i] < 3:
                result.append(60)
            else:
                result.append(grades[i])
        elif grades[i] < 65:
            if 65 - grades[i] < 3:
                result.append(65)
            else:
                result.append(grades[i])
        elif grades[i] < 70:
            if 70 - grades[i] < 3:
                result.append(70)
            else:
                result.append(grades[i])
        elif grades[i] < 75:
            if 75 - grades[i] < 3:
                result.append(75)
            else:
                result.append(grades[i])
        elif grades[i] < 80:
            if 80 - grades[i] < 3:
                result.append(80)
            else:
                result.append(grades[i])
        elif grades[i] < 85:
            if 85 - grades[i] < 3:
                result.append(85)
            else:
                result.append(grades[i])
        elif grades[i] < 90:
            if 90 - grades[i] < 3:
                result.append(90)
            else:
                result.append(grades[i])
        elif grades[i] < 95:
            if 95 - grades[i] < 3:
                result.append(95)
            else:
                result.append(grades[i])
        elif grades[i] < 100:
            if 100 - grades[i] < 3:
                result.append(100)
            else:
                result.append(grades[i])
        i = i + 1
    return result


def main():
    n = int(input("Insert n"))
    grades = []
    for _ in range(n):
        grades_item = int(input())
        grades.append(grades_item)

    result = gradingStudents(grades)
    print(result)

main()