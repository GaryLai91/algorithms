def get_data(filename):
    data = []
    with open(filename, 'r') as f:
        num_lines = int(f.readline())
        for i in range(num_lines):
            line = f.readline()
            arr = [int(i) for i in line.split(" ")]
            data.append((arr[0], arr[1]))
    return data


def greedy_diff(weight, length):
    return weight - length


def greedy_ratio(weight, length):
    return weight / length


def schedule(data, func=None):
    # (score, w, l)
    completion_time = 0
    diff_score = []
    for (w, l) in data:
        score = func(w, l)
        diff_score.append((score, w, l))
    sorted_diff_score = sorted(diff_score,
                               key=lambda x: (x[0], x[1]),
                               reverse=True)
    total_job_length = 0
    for job in sorted_diff_score:
        completion_time += job[1] * (job[2] + total_job_length)
        total_job_length += job[2]
    return completion_time
