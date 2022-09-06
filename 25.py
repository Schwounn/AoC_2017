import collections


def read_input():
    raw = [line.strip() for line in open('25.in')]
    start = raw[0][-2]
    diagnostic = int(raw[1].split()[-2])
    states = {}
    for i in range(3, len(raw), 10):
        state = raw[i][-2]
        actions = {}
        for data in range(2):
            ind = i + 4 * data + 1
            wr = int(raw[ind + 1][-2])
            move = raw[ind + 2].split()[-1][:-1]
            n = raw[ind + 3][-2]
            actions[data] = {'write': wr,
                             'move': move,
                             'next': n}
        states[state] = actions
    return start, diagnostic, states


def turing(tape, state, head, prog):
    actions = prog[state][tape[head]]
    tape[head] = actions['write']
    if actions['move'] == 'right':
        head += 1
    else:
        head -= 1
    return actions['next'], head, tape


def part1():
    state, diagnostic, prog = read_input()
    tape = collections.defaultdict(int)
    head = 0
    for i in range(diagnostic):
        state, head, tape = turing(tape, state, head, prog)
    return sum(tape.values())


if __name__ == '__main__':
    print(part1())