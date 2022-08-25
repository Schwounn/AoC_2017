import collections
import re

def read_input():
    raw = [line.strip() for line in open('20.in')]
    ret = []
    pattern =r"p=<([^>]*)>, v=<([^>]*)>, a=<([^>]*)>"
    for line in raw:
        m = re.match(pattern, line).groups()
        particle = [tuple(map(int, vec)) for vec in map(lambda x: x.split(','), m)]
        ret.append(dict(zip('pva', particle)))
    return ret

def vec_add(a, b):
    return tuple(map(sum, zip(a, b)))


def vec_sub(a, b):
    return tuple(map(lambda i: i[0] - i[1], zip(a, b)))


def get_next_cycle(particle):
    particle['v'] = vec_add(particle['v'], particle['a'])
    particle['p'] = vec_add(particle['v'], particle['p'])
    return particle

def part1():
    data = read_input()
    best = float('inf')
    best_i = 0
    for i, partic in enumerate(data):
        a = sum(map(abs, partic['a']))
        if a < best:
            best_i = i
            best = a
    return best_i


def part2():
    data = dict(enumerate(read_input()))
    for i in range(10000):
        counts = collections.defaultdict(int)
        for p, particle in data.items():
            data[p] = get_next_cycle(particle)
            counts[particle['p']] += 1
        for pos, count in counts.items():
            if count <= 1:
                continue
            for p, particle in [a for a in data.items()]:
                if particle['p'] == pos:
                    del data[p]

    return len(data)


if __name__ == '__main__':
    print(part1(), part2())

