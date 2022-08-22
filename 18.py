import collections
import copy

class Comp:
    def __init__(self, prog, id):
        self.pc = 0
        self.prog = copy.copy(prog)
        self.regs = collections.defaultdict(int)
        self.regs['p'] = id
        self.in_buffer = []
        self.out_buffer = []
        self.send_count = 0

    def execute(self):
        while True:
            op = self.prog[self.pc]
            if op[0] == 'set':
                self.regs[op[1]] = inter(op[2], self.regs)
                self.pc += 1
            elif op[0] == 'snd':
                self.out_buffer.append(inter(op[1], self.regs))
                self.pc += 1
                self.send_count += 1
            elif op[0] == 'add':
                self.regs[op[1]] += inter(op[2], self.regs)
                self.pc += 1
            elif op[0] == 'mul':
                self.regs[op[1]] *= inter(op[2], self.regs)
                self.pc += 1
            elif op[0] == 'mod':
                self.regs[op[1]] %= inter(op[2], self.regs)
                self.pc += 1
            elif op[0] == 'rcv':
                try:
                    self.regs[op[1]] = self.in_buffer.pop(0)
                except IndexError as e:
                    return
                self.pc += 1
            elif op[0] == 'jgz':
                if inter(op[1], self.regs) > 0:
                    self.pc += inter(op[2], self.regs)
                else:
                    self.pc += 1


def read_input():
    return [line.strip().split() for line in open('18.in')]


def inter(key : str, regs : collections.defaultdict):
    if key.isalpha():
        return regs[key]
    else:
        return int(key)


def execute(prog, pc, regs, old_snd):
    regs = copy.copy(regs)
    op = prog[pc]
    snd = None
    rcv = None
    if op[0] == 'set':
        regs[op[1]] = inter(op[2], regs)
        pc += 1
    elif op[0] == 'snd':
        snd = inter(op[1], regs)
        pc += 1
    elif op[0] == 'add':
        regs[op[1]] += inter(op[2], regs)
        pc += 1
    elif op[0] == 'mul':
        regs[op[1]] *= inter(op[2], regs)
        pc += 1
    elif op[0] == 'mod':
        regs[op[1]] %= inter(op[2], regs)
        pc += 1
    elif op[0] == 'rcv':
        if inter(op[1], regs) != 0:
            rcv = old_snd
        pc += 1
    elif op[0] == 'jgz':
        if inter(op[1], regs) > 0:
            pc += inter(op[2], regs)
        else:
            pc += 1
    return pc, regs, snd, rcv

def part1():
    prog = read_input()
    pc = 0
    regs = collections.defaultdict(int)
    old_snd = None
    while True:
        pc, regs, snd, rcv = execute(prog, pc, regs, old_snd)
        if snd is not None:
            old_snd = snd
        if rcv is not None:
            return rcv


def part2():
    data = read_input()
    comp0, comp1 = Comp(data, 0), Comp(data, 1)
    while True:
        comp0.execute()
        comp1.execute()
        if len(comp0.out_buffer) == 0 and len(comp1.out_buffer) == 0:
            return comp1.send_count
        comp0.in_buffer = comp0.in_buffer + comp1.out_buffer
        comp1.out_buffer = []
        comp1.in_buffer = comp1.in_buffer + comp0.out_buffer
        comp0.out_buffer = []


if __name__ == '__main__':
    print(part1(), part2())