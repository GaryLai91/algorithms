"""
Count Inversions
"""


def brute_force(ls):
    """
    Brute force implementation
    """
    count = 0
    for i in range(len(ls) - 1):
        for j in range(i + 1, len(ls)):
            if ls[i] > ls[j]:
                count += 1
    return count


def count_split_inv(C, D):
    n = len(C) + len(D)
    B = []
    count = 0
    i = j = 0
    while i < len(C) and j < len(D):
        if C[i] < D[j]:
            B.append(C[i])
            i += 1
        elif D[j] < C[i]:
            B.append(D[j])
            j += 1
            count += (n//2 - i)
    if i != len(C):
        B.extend(C[i:])
    if j != len(D):
        B.extend(D[j:])

    return B, count


def count_inv(A):
    """
    Divide and Conquer implementation
    """
    if len(A) <= 1:
        return A, 0
    else:
        C, left_inv = count_inv(A[:len(A)//2])
        D, right_inv = count_inv(A[len(A)//2:])
        B, split_inv = count_split_inv(C, D)
        return B, left_inv + right_inv + split_inv


if __name__ == "__main__":
    print(count_inv([8, 7, 6, 5, 4, 3, 2, 1]))
