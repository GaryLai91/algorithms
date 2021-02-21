from algorithms.job_scheduling import get_data, greedy_diff, greedy_ratio, schedule
import pytest
import glob

all_files = glob.glob("input_random_*.txt")


def get_output(filename):
    output = []
    with open(filename, "r") as f:
        lines = f.readlines()
        for line in lines:
            d = int(line)
            output.append(d)
    return output


@pytest.mark.parametrize("filename", all_files)
def test_case(filename):
    data = get_data(filename)
    output = get_output(filename.replace("input", "output"))
    diff = schedule(data, greedy_diff)
    ratio = schedule(data, greedy_ratio)
    assert diff == output[0] and ratio == output[1]


if __name__ == "__main__":
    data = get_data("challenge.txt")
    diff = schedule(data, greedy_diff)
    ratio = schedule(data, greedy_ratio)
    print(f"diff: {diff}")
    print(f"ratio: {ratio}")