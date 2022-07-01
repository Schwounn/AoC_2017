
def read_input():
    return [int(c) for c in open('01.in').read().strip()]


def part1():
    data = read_input()
    ret = 0
    for i, v in enumerate(data):
        if v == data[(i + 1) % len(data)]:
            ret += v
    return ret


def part2():
    data = read_input()
    ret = 0
    for i, v in enumerate(data):
        if v == data[(i + len(data) // 2) % len(data)]:
            ret += v
    return ret


if __name__ == '__main__':
    print(part1(), part2())