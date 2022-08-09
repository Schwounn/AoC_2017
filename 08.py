from collections import defaultdict
def read_input():
    return [line.strip().split() for line in open('08.in')]


def intr(val, regs):
    if val.isalpha():
        return regs[val]
    return int(val)


def part1():
    data = read_input()
    regs = defaultdict(int)
    ret = 0
    for line in data:
        ins = line[1]
        a, op, b = line[4:]
        if eval(f"intr(a, regs) {op} intr(b, regs)"):
            if ins == 'inc':
                regs[line[0]] += intr(line[2], regs)
            else:
                regs[line[0]] -= intr(line[2], regs)
    return max(regs.values())

def part2():
    data = read_input()
    regs = defaultdict(int)
    ret = 0
    for line in data:
        ins = line[1]
        a, op, b = line[4:]
        if eval(f"intr(a, regs) {op} intr(b, regs)"):
            if ins == 'inc':
                regs[line[0]] += intr(line[2], regs)
                ret = max(ret, regs[line[0]])
            else:
                regs[line[0]] -= intr(line[2], regs)
                ret = max(ret, regs[line[0]])
    return ret



if __name__ == '__main__':
    print(part1(), part2())