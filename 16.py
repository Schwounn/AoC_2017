import copy


def read_input():
    raw = open('16.in').read().strip().split(',')
    ret = []
    for cmd in raw:
        op = cmd[0]
        if op == 's' or op == 'x':
            args = tuple(map(int, cmd[1:].split('/')))
        else:
            args = cmd[1:].split('/')
        ret.append((op, *args))
    return ret

def execute_dance(ops, world):
    world = copy.copy(world)
    for op in ops:
        o = op[0]
        if o == 's':
            i = op[1]
            world = world[-i:] + world[:-i]
        elif o == 'x':
            ai, bi = op[1:]
            world[bi], world[ai] = world[ai], world[bi]
        else:
            ai, bi = world.index(op[1]), world.index(op[2])
            world[bi], world[ai] = world[ai], world[bi]
    return world


def part1():
    ops = read_input()
    world = [chr(ord('a') + i) for i in range(16)]
    world = execute_dance(ops, world)
    return ''.join(world)


def part2():
    ops = read_input()
    start = [chr(ord('a') + i) for i in range(16)]
    world = execute_dance(ops, start)
    cycle_len = 1
    while ''.join(start) != ''.join(world):
        cycle_len += 1
        world = execute_dance(ops, world)
    billion = 1_000_000_000
    actual_dance_len = billion % cycle_len
    for i in range(actual_dance_len):
        world = execute_dance(ops, world)
    return ''.join(world)


if __name__ == '__main__':
    print(part1(), part2())