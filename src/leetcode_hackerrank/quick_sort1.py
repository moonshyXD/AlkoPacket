#!/bin/python3

import os

#
# Complete the 'quickSort' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#


def quickSort(arr: list[int]) -> list[int]:
    if len(arr) <= 1:
        return arr

    less_than = []
    higher_than = []
    equal = []
    pivot = arr[len(arr) // 2]
    for number in arr:
        if number > pivot:
            higher_than.append(number)
        elif number < pivot:
            less_than.append(number)
        else:
            equal.append(number)

    return quickSort(less_than) + equal + quickSort(higher_than)


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = quickSort(arr)

    fptr.write(" ".join(map(str, result)))
    fptr.write("\n")

    fptr.close()
