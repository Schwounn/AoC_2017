import math


def read_input():
    raw = [line.strip() for line in open('15.in')]
    return int(raw[0].split()[-1]), int(raw[1].split()[-1])


def get_next(data, factors, divider):
    return tuple(map(lambda x: math.prod(x) % divider, zip(data, factors)))


def get_lowest_bits(i, bits=16):
    return bin(i)[2:].zfill(bits)[-16:]

def part1():
    data = read_input()
    factors = (16807, 48271)
    divider = 2147483647
    ret = 0
    for i in range(40_000_000):
        data = get_next(data, factors, divider)
        bstrs = tuple(map(get_lowest_bits, data))
        if bstrs[0] == bstrs[1]:
            ret += 1
    return ret


def get_next2(data, factors, divider, mods=(4, 8)):
    a, b = data
    a = (a * factors[0]) % divider
    b = (b * factors[1]) % divider
    while a % mods[0] != 0:
        a = (a * factors[0]) % divider
    while b % mods[1] != 0:
        b = (b * factors[1]) % divider
    return a, b

def part2():
    data = read_input()
    factors = (16807, 48271)
    divider = 2147483647
    ret = 0
    for i in range(5_000_000):
        data = get_next2(data, factors, divider)
        bstrs = tuple(map(get_lowest_bits, data))
        if bstrs[0] == bstrs[1]:
            ret += 1
    return ret



if __name__ == '__main__':
    print(part1(), part2())