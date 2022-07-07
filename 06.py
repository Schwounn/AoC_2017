
def read_input():
    return tuple(map(int, open('06.in').read().split()))

def get_next(data):
    highest = max(data)
    index = data.index(max(data))
    next_l = list(data)
    next_l[index] = 0
    while highest:
        index += 1
        next_l[index % len(next_l)] += 1
        highest -= 1
    return tuple(next_l)


def part1():
    data = read_input()
    visited = set()
    visited.add(data)
    ret = 0
    while True:
        data = get_next(data)
        ret += 1
        if data in visited:
            return ret
        visited.add(data)


def part2():
    data = read_input()
    visited = []
    visited.append(data)
    ret = 0
    while True:
        data = get_next(data)
        ret += 1
        if data in visited:
            return ret - visited.index(data)
        visited.append(data)



if __name__ == '__main__':
    print(part1(), part2())