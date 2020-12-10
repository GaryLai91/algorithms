from quicksort import partition
from random import randint


def RSelect(arr, l, r, k):
    if len(arr) == 1:
        return arr[0]
    if l > r:
        i = l
    else:
        i = randint(l, r)
    print(f"i : {i}")
    arr[l], arr[i] = arr[i], arr[l]
    j = partition(arr, l, r)
    if j + 1 == k:
        print(arr)
        return arr[j]
    elif j > k:
        return RSelect(arr, l, j - 1, k)
    else:
        return RSelect(arr, j + 1, r, k)


# Might enco
# RecursionError: maximum recursion depth exceeded while calling a Python object
