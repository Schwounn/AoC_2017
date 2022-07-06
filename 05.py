
def read_input():
    return [int(line.strip()) for line in open('05.in')]

def part1():
    pc = 0
    data = read_input()
    i = 0
    while pc >= 0 and pc < len(data):
        offset = data[pc]
        data[pc] += 1
        pc += offset
        i += 1
    return i


def part2():
    pc = 0
    data = read_input()
    i = 0
    while pc >= 0 and pc < len(data):
        offset = data[pc]
        if offset >= 3:
            data[pc] -= 1
        else:
            data[pc] += 1
        pc += offset
        i += 1
    return i


if __name__ == '__main__':
    print(part1(), part2())
