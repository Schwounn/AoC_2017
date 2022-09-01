
def read_input():
    return [line.strip().split() for line in open('23.in')]


def inter(key : str, regs):
    if key.isalpha():
        return regs[key]
    return int(key)


def part1():
    prog = read_input()
    pc = 0
    regs = {chr(ord('a') + i) : 0 for i in range(8)}
    ret = 0
    while True:
        op, a, b = prog[pc]
        if op == 'set':
            regs[a] = inter(b, regs)
            pc += 1
        elif op == 'sub':
            regs[a] -= inter(b, regs)
            pc += 1
        elif op == 'mul':
            regs[a] *= inter(b, regs)
            pc += 1
            ret += 1
        elif op == 'jnz':
            if inter(a, regs) != 0:
                pc += inter(b, regs)
            else:
                pc += 1
        if pc >= len(prog):
            return ret

def primes(upper):
    sieve = [True] * (upper + 1)
    sieve[0] = False
    sieve[1] = False
    p = 2
    while p <= upper**0.5:
        if not sieve[p]:
            p += 1
            continue
        for i in range(p * 2, upper + 1, p):
            sieve[i] = False
        p += 1

    return {i for i in range(upper + 1) if sieve[i]}


def part2():
    lower = 67*100 + 100000
    upper = lower + 17000
    prs = primes(upper)
    return sum([1 for i in range(lower, upper + 1, 17) if i not in prs])


def fake():
    a = 1
    h = 0
    b = 67
    c = b
    if a != 0:
        b = b * 100 + 100000
        c = b + 17000

    f = 1 # 9
    d = 2

    e = 2 # 11

    g = d*e -b # 12
    if g == 0:
        f = 0
    e += 1
    g = e
    g -= b

    # 20 goto 12 b-2 times
    d += 1
    g = d - b

    # 24 goto 11 b-2 times
    if f == 0:
        h += 1
    g = b - c
    if g == 0:
        return h
    b += 17
    # 32 goto 9


if __name__ == '__main__':
    print(part1(), part2())

