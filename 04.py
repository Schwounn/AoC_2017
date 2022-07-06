
def read_input():
    return [line.strip().split() for line in open('04.in')]


def part1():
    data = read_input()
    return sum([1 for line in data if len(line) == len(set(line))])


def part2():
    data = read_input()
    data = [list(map(lambda x: ''.join(sorted(x)), line)) for line in data]
    return sum([1 for line in data if len(line) == len(set(line))])


if __name__ == '__main__':
    print(part1(), part2())