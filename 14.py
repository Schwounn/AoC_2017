import functools


def read_input():
    return open('14.in').read().strip()


def knot_hash(data):
    data = data + [17, 31, 73, 47, 23]
    l = list(range(256))
    cp = 0
    skip = 0
    for length in data * 64:
        start, stop = cp, cp + length
        if stop > len(l):
            rev = list(reversed(l[start:] + l[:stop % len(l)]))
            for i in range(start, stop):
                l[i % len(l)] = rev[i - start]
        else:
            rev = list(reversed(l[start:stop]))
            l[start:stop] = rev
        cp = (cp + length + skip) % len(l)
        skip += 1
    dense = []
    for i in range(16):
        dense.append(functools.reduce(lambda a, b: a ^ b, l[i * 16:(i + 1) * 16]))

    return "".join(map(lambda i: f"{i:02X}", dense))


def get_parent(i, djs):
    if djs[i] == i:
        return i
    gp = get_parent(djs[i], djs)
    return gp

def union_djs(a, b, djs):
    pa = get_parent(a, djs)
    pb = get_parent(b, djs)
    djs[pb] = pa

def part1():
    data = read_input()
    ret = 0
    for i in range(128):
        s = list(map(ord, data + f"-{i}"))
        hash = knot_hash(s)
        binary = bin(int(hash, 16))[2:].zfill(len(hash) * 4)
        ret += binary.count('1')
    return ret


def get_neighbors(x, y, grid):
    dn = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    ret = []
    for dx, dy in dn:
        nx, ny = x + dx, y + dy
        if nx < 0 or nx >= len(grid[0]) or ny < 0 or ny >= len(grid):
            continue
        if grid[ny][nx] != '1':
            continue
        ret.append((nx, ny))
    return ret


def part2():
    data = read_input()
    grid = []
    for i in range(128):
        s = list(map(ord, data + f"-{i}"))
        hash = knot_hash(s)
        binary = bin(int(hash, 16))[2:].zfill(len(hash) * 4)
        grid.append(binary)
        #print(binary)

    djs = {}
    for y, line in enumerate(grid):
        for x, c in enumerate(line):
            if c == '1':
                djs[(x, y)] = (x, y)

    for y, line in enumerate(grid):
        for x, c in enumerate(line):
            if c != '1':
                continue
            for nx, ny in get_neighbors(x, y, grid):
                union_djs((x, y), (nx, ny), djs)
    groups = {get_parent(key, djs) for key in djs}
    return len(groups)


if __name__ == '__main__':
    print(part1(), part2())