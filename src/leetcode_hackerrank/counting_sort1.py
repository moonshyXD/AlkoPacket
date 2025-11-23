#!/bin/python3

import os


def countingSort(arr: list[int]) -> list[int]:
    n = 100
    lst = [0] * (n)
    for i in arr:
        lst[i] += 1

    return lst


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = countingSort(arr)

    fptr.write(" ".join(map(str, result)))
    fptr.write("\n")

    fptr.close()
