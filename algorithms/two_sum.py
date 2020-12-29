data = [
    46099924748,
    -46099917034,
    73636268024,
    46099921372,
    2190350483,
    -80066206438,
    89786393815,
    59624633529,
    1178006368,
    -88867066418,
]

data2 = [-3, -1, 1, 2, 9, 11, 7, 6, 2]


def preprocess(data):
    d = {}
    for i in data:
        try:
            d[i] += 1
        except KeyError:
            d[i] = 1
    return d


def solve(data, target=(0, 0)):
    d = preprocess(data)
    set_of_keys = set()
    for x in d.keys():
        if d[x] != 0:
            for t in range(target[0], target[1] + 1):
                y = t - x
                try:
                    d[y]
                except KeyError:
                    continue
                else:
                    if x > y:
                        set_of_keys.add((y, x))
                    else:
                        set_of_keys.add((x, y))
    return len(set_of_keys)


if __name__ == "__main__":
    # print(solve(data, (-10000, 10000)))
    print(solve(data2, (3, 10)))
