
def read_input():
    raw = [line.strip() for line in open('12.in')]
    ret = {}
    for line in raw:
        lh, rh = line.split('<->')
        lh = int(lh)
        rh = list(map(int, rh.split(',')))
        ret[lh] = rh
    return ret

def get_parent(i, djs):
    if djs[i] == i:
        return i
    gp = get_parent(djs[i], djs)
    return gp


def part1():
    data = read_input()
    djs = {i: i for i in data}
    for key in data:
        for con in data[key]:
            child, parent = max(con, key), min(con, key)
            if djs[child] != child:
                parent, child = child, parent
            djs[get_parent(child, djs)] = get_parent(parent, djs)
    return sum([1 for i in data if get_parent(i, djs) == get_parent(0, djs)])


def part2():
    data = read_input()
    djs = {i: i for i in data}
    for key in data:
        for con in data[key]:
            child, parent = max(con, key), min(con, key)
            if djs[child] != child:
                parent, child = child, parent
            djs[get_parent(child, djs)] = get_parent(parent, djs)
    parent_groups = {get_parent(i, djs) for i in data}
    return len(parent_groups)


if __name__ == '__main__':
    print(part1(), part2())