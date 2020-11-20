from random import randint


def partition(A, l, r):
    """
    This subroutine takes as input array A
    but operates only on subarray of elements A[l] to A[r],
    partitions such that elements before A[l] is less than A[l].
    """
    p = A[l]
    i = l + 1
    for j in range(i, r + 1):
        if A[j] < p:
            A[j], A[i] = A[i], A[j]
            i += 1
    A[l], A[i - 1] = A[i - 1], A[l]
    return i - 1


def choose_pivot_first(A, l, r):
    return l


def choose_pivot_last(A, l, r):
    return r


def choose_pivot_random(A, l, r):
    return randint(l + 1, r - 1)


def choose_pivot_median(A, l, r):
    # arr = sorted([A[l], A[r], A[r // 2]])
    # return A.index(arr[1])
    mid = (r + l) // 2
    if A[l] <= A[mid] <= A[r]:
        return mid
    if A[r] <= A[mid] <= A[l]:
        return mid
    if A[l] <= A[r] <= A[mid]:
        return r
    if A[mid] <= A[r] <= A[l]:
        return r
    return l


def choose_pivot(A, l, r, method="first"):
    if method == "first":
        pivot = choose_pivot_first(A, l, r)
    elif method == "last":
        pivot = choose_pivot_last(A, l, r)
    elif method == "random":
        pivot = choose_pivot_random(A, l, r)
    elif method == "median":
        pivot = choose_pivot_median(A, l, r)
    return pivot


def Quicksort(A, l, r, method):
    count = 0
    if l >= r:
        return count
    i = choose_pivot(A, l, r, method)
    A[l], A[i] = A[i], A[l]
    j = partition(A, l, r)
    count += Quicksort(A, l, j - 1, method)
    count += Quicksort(A, j + 1, r, method)
    return count + r - l

