def get_input(filename):
    output = []
    with open(filename, "r") as f:
        _ = f.readline()
        lines = f.readlines()
        for line in lines:
            output.append(int(line.strip()))
    return output


def wis(weight):
    result = [0] * (len(weight) + 1)
    result[0] = 0
    result[1] = weight[0]
    for i in range(2, len(result)):
        first_case = result[i - 1]
        second_case = result[i - 2] + weight[i - 1]
        result[i] = max(first_case, second_case)
    return result


def wis_reconstruct(weight, result):
    s = set()
    i = len(weight)
    while i >= 2:
        if result[i - 1] >= result[i - 2] + weight[i - 1]:
            i -= 1
        else:
            s.add(weight[i - 1])
            i -= 2
    if i == 1:
        s.add(weight[0])
    return s


def parse_output(weight, s):
    output = [0] * 8
    idx = [1, 2, 3, 4, 17, 117, 517, 997]
    vertices = []
    for i in idx:
        if i <= len(weight):
            vertices.append(weight[i - 1])
    for i in range(len(vertices)):
        if vertices[i] in s:
            output[i] = 1
    return "".join([str(i) for i in output])


def get_mwis(weight):
    result = wis(weight)
    mwis = wis_reconstruct(weight, result)
    return parse_output(weight, mwis)


if __name__ == "__main__":
    weight = get_input("test.txt")
    print(get_mwis(weight))