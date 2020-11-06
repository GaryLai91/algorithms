def karat(x, y):
    if len(str(x)) == 1 or len(str(y)) == 1:
        return x * y
    else:
        m = max(len(str(x)), len(str(y)))
        m2 = m // 2

        a = x // 10 ** (m2)
        b = x % 10 ** (m2)
        c = y // 10 ** (m2)
        d = y % 10 ** (m2)

        z0 = karat(b, d)
        z1 = karat((a + b), (c + d))
        z2 = karat(a, c)

        return (z2 * 10 ** (2 * m2)) + ((z1 - z2 - z0) * 10 ** (m2)) + (z0)


if __name__ == "__main__":
    x1 = 3141592653589793238462643383279502884197169399375105820974944592
    x2 = 2718281828459045235360287471352662497757247093699959574966967627
    product = karat(x1, x2)
    actual = x1 * x2
    print(product)
    print(product == actual)
