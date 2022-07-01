
def read_input():
    return [[int(i) for i in line.strip().split()] for line in open('02.in')]


def part1():
    data = read_input()
    return sum([max(row) - min(row) for row in data])


def part2():
    data = read_input()
    ret = 0
    for row in data:
        for i, a in enumerate(row):
            for j, b in enumerate(row):
                if i != j and a % b == 0:
                    ret += a // b
                    break
    return ret

if __name__ == '__main__':
    print(part1(), part2())