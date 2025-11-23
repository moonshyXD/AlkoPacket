#!/bin/python3

import os

#
# Complete the 'countingSort' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#


def countingSort(arr: list[int]) -> list[int]:
    n = max(arr)
    lst = [0] * (n + 1)
    for i in arr:
        lst[i] += 1

    result: list[int] = []
    for i in range(n + 1):
        result.extend([i] * lst[i])

    return result


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = countingSort(arr)

    fptr.write(" ".join(map(str, result)))
    fptr.write("\n")

    fptr.close()
