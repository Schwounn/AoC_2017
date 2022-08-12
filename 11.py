
d_to_vec = {
    'ne': (1, -1, 0),
    'se': (1, 0, -1),
    's': (0, 1, -1),
    'sw': (-1, 1, 0),
    'nw': (-1, 0, 1),
    'n': (0, -1, 1),
}

def read_input():
    return open('11.in').read().strip().split(',')


def vec_add(a, b):
    return tuple(map(sum, zip(a, b)))


def vec_sub(a, b):
    return tuple(map(lambda a: a[0] - a[1], zip(a, b)))


def dist(a, b):
    diff = vec_sub(b, a)
    return sum(map(abs, diff)) // 2


def part1():
    data = read_input()
    pos = (0, 0, 0)
    for d in data:
        pos = vec_add(pos, d_to_vec[d])
    return dist((0, 0, 0), pos)


def part2():
    data = read_input()
    pos = (0, 0, 0)
    ret = 0
    for d in data:
        pos = vec_add(pos, d_to_vec[d])
        ret = max(ret, dist((0, 0, 0), pos))
    return ret



if __name__ == '__main__':
    print(part1(), part2())