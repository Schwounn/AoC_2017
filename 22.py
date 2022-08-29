import collections


def read_input():
    raw = [line.strip() for line in open('22.in')]
    offsetx = len(raw[0]) // 2
    offsety = len(raw) // 2
    ret = {(x - offsetx, y - offsety) for y in range(len(raw)) for x in range(len(raw[0])) if raw[y][x] == '#'}
    return ret


def vec_add(a, b):
    return tuple(map(sum, zip(a, b)))


def vec_sub(a, b):
    return tuple(map(lambda i: i[0] - i[1], zip(a, b)))


def turn(direction, t):
    if t == 'l':
        return (direction[1], -direction[0])
    else:
        return (-direction[1], direction[0])


def part1():
    data = read_input()
    pos = (0, 0)
    direction = (0, -1)
    ret = 0
    for i in range(10_000):
        if pos in data:
            direction = turn(direction, 'r')
            data.remove(pos)
        else:
            direction = turn(direction, 'l')
            data.add(pos)
            ret += 1
        pos = vec_add(direction, pos)
    return ret


def part2():
    data = read_input()
    grid = collections.defaultdict(lambda: '.')
    for coord in data:
        grid[coord] = '#'
    pos = (0, 0)
    direction = (0, -1)
    ret = 0
    for i in range(10_000_000):
        if grid[pos] == '#':
            direction = turn(direction, 'r')
            grid[pos] = 'F'
        elif grid[pos] == '.':
            direction = turn(direction, 'l')
            grid[pos] = 'W'
        elif grid[pos] == 'W':
            grid[pos] = '#'
            ret += 1
        else:
            direction = vec_sub((0, 0), direction)
            grid[pos] = '.'
        pos = vec_add(direction, pos)
    return ret



if __name__ == '__main__':
    print(part1(), part2())