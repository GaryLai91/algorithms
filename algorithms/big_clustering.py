from collections import defaultdict
from union_find import UF


def get_bin_input(filename):
    graph = defaultdict(list)
    with open(filename, 'r') as f:
        n = [int(i) for i in f.readline().strip().split(" ")]
        for i in range(1, n[0] + 1):
            line = f.readline()
            bin_str = line.strip().replace(" ", "")
            graph[bin_str].append(i)
    return n[0], graph


def compute_one_distance(binary_string):
    """
    args: binary_string
        binary_string = "1000"
    """
    bin_str = [i for i in binary_string]
    combs = []
    for i in range(len(bin_str)):
        c = bin_str[:]
        if bin_str[i] == '0':
            c[i] = "1"
        else:
            c[i] = "0"
        combs.append(c)
    d = {''.join(i): 1 for i in combs}
    return d


def compute_two_distance(binary_string):
    """
    args: binary_string
        binary_string = "1000"
    """
    bin_str = [i for i in binary_string]
    two_combs = []
    for i in range(len(bin_str)):
        c = bin_str[:]
        if c[i] == '0':
            c[i] = '1'
        else:
            c[i] = '0'
        for j in range(len(bin_str)):
            d = c[:]
            if i == j:
                continue
            if bin_str[j] == '0':
                d[j] = "1"
            else:
                d[j] = "0"
            two_combs.append(d)
    d = {''.join(i): 1 for i in two_combs}
    return d


def clustering(n, input_data):
    """
    args: input_data
        input_data = {'0000100110': [1,2], '0110101100': [3,4] , 
                      '1000100110' : [5], ... }
    """
    uf = UF(n)
    input_dict = {k: v for k, v in input_data.items()}

    # Merge all 0 distance
    for bin_str, u_vertices in input_dict.items():
        try:
            input_dict[bin_str]
        except KeyError:
            continue
        else:
            v_vertices = input_dict[bin_str]
            for u in u_vertices:
                for v in v_vertices:
                    if (uf.find(u - 1) != uf.find(v - 1)):
                        uf.union(u - 1, v - 1)

    # Merge all 1 distance
    for bin_str, u_vertices in input_dict.items():
        one_comb = compute_one_distance(bin_str)
        for node in one_comb:
            try:
                input_dict[node]
            except KeyError:
                continue
            else:
                v_vertices = input_dict[node]
                for u in u_vertices:
                    for v in v_vertices:
                        if (uf.find(u - 1) != uf.find(v - 1)):
                            uf.union(u - 1, v - 1)

    # Merge all 2 distances
    for bin_str, u_vertices in input_dict.items():
        two_comb = compute_two_distance(bin_str)
        for node in two_comb:
            try:
                input_dict[node]
            except KeyError:
                continue
            else:
                v_vertices = input_dict[node]
                for u in u_vertices:
                    for v in v_vertices:
                        if uf.find(u - 1) != uf.find(v - 1):
                            uf.union(u - 1, v - 1)
    return len(uf.get_clusters())
