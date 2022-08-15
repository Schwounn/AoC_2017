
def read_input():
    spl = [list(map(int, line.strip().split(':'))) for line in open('13.in')]
    return dict(spl)


def get_severity(delay=0, data=read_input()):
    tot_cost = 0
    is_caught = False
    for layer in range(0, max(data) + 1):
        if layer not in data:
            continue
        arrival = layer + delay
        period = (data[layer] - 1) * 2
        if arrival % period == 0:
            is_caught = True
            tot_cost += layer * data[layer]

    return tot_cost, is_caught

def part1():
    data = read_input()
    return get_severity(delay=0, data=data)[0]


def part2():
    data = read_input()
    i = 0
    while True:
        s, is_caught = get_severity(delay=i, data=data)
        if not is_caught:
            return i
        i += 1


if __name__ == '__main__':
    print(part1(), part2())