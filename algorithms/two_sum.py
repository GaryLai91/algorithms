def preprocess(data):
    d = {}
    for i in data:
        try:
            d[i] += 1
        except KeyError:
            d[i] = 1
    return d


def solve(data, target=(-10000, 10000)):
    d = preprocess(data)
    count = 0
    for t in range(target[0], target[1] + 1):
        for x in d.keys():
            y = t - x
            try:
                d[y]
            except KeyError:
                continue
            else:
                if x != y:
                    count += 1
                    break
    return count