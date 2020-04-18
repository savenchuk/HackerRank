"""Objective
Today, we're learning about the Array data structure.

Task
Given an array, A, of N integers, print A's elements in reverse order
as a single line of space-separated numbers.
"""


if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    arr.reverse()
    for num in arr:
        print(num, end=' ')
