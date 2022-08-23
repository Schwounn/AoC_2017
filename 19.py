
def read_input():
    raw = [line.rstrip() for line in open('19.in')]
    return raw


def get_neighbors(x, y, grid):
    dn = [(dx, dy) for dx in [-1, 0, 1] for dy in [-1, 0, 1] if (dx == 0 or dy == 0) and dx != dy]
    ret = []
    for dx, dy in dn:
        nx, ny = x + dx, y + dy
        try:
            ret.append((nx, ny, grid[ny][nx]))
        except IndexError:
            pass
    return ret


def get_start(grid):
    for y, line in enumerate(grid):
        for x, c in enumerate(line):
            if c != ' ':
                return x, y


def vec_add(a, b):
    return tuple(map(sum, zip(a, b)))


def vec_sub(a, b):
    return tuple(map(lambda i: i[0] - i[1], zip(a, b)))

def part1():
    data = read_input()
    x, y = get_start(data)[:2]
    direction = (0, 1)
    ret = []
    while True:
        nx, ny = vec_add(direction, (x, y))
        nc = data[ny][nx]
        if nc.isalpha():
            ret.append(nc)
        elif nc == ' ':
            return ''.join(ret)
        elif nc == '+':
            for n in get_neighbors(nx, ny, data):
                if n[2] == ' ':
                    continue
                new_direction = vec_sub(n[:2], (nx, ny))
                if new_direction != vec_sub((0, 0), direction):
                    direction = new_direction
                    break
        x, y = nx, ny


def part2():
    data = read_input()
    x, y = get_start(data)[:2]
    direction = (0, 1)
    ret = 0
    while True:
        nx, ny = vec_add(direction, (x, y))
        nc = data[ny][nx]
        ret += 1
        if nc == ' ':
            return ret
        elif nc == '+':
            for n in get_neighbors(nx, ny, data):
                if n[2] == ' ':
                    continue
                new_direction = vec_sub(n[:2], (nx, ny))
                if new_direction != vec_sub((0, 0), direction):
                    direction = new_direction
                    break
        x, y = nx, ny



if __name__ == '__main__':
    print(part1(), part2())