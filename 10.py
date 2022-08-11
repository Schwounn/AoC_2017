import functools
import math
import itertools

def read_input():
    return list(map(int, open('10.in').read().strip().split(',')))


def read_input2():
    return list(map(ord, open('10.in').read().strip())) + [17, 31, 73, 47, 23]

def part1():
    data = read_input()
    l = list(range(256))
    cp = 0
    skip = 0
    for length in data:
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
    return math.prod(l[:2])

def part2():
    data = read_input2()
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
        dense.append(functools.reduce(lambda a, b: a^b, l[i * 16:(i + 1) * 16]))

    return "".join(map(lambda i: f"{i:02X}", dense))



if __name__ == '__main__':
    print(part1(), part2())