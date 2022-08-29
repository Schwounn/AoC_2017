
def read_input():
    raw = [line.strip().split(' => ') for line in open('21.in')]
    return dict([map(lambda s: tuple(s.split('/')), line) for line in raw])


def div_grid(grid):
    ret = []
    if len(grid) % 2 == 0:
        sz = 2
    else:
        sz = 3
    for y in range(0, len(grid), sz):
        row = []
        for x in range(0, len(grid[0]), sz):
            box = tuple([line[x:x+sz] for line in grid[y:y+sz]])
            row.append(box)
        ret.append(row)
    return ret


def flip(box):
    return tuple(zip(*box))


def rotate(box):
    ret = [[None] * len(box) for i in range(len(box))]
    for y in range(len(box)):
        for x in range(len(box)):
            ret[y][x] = box[x][-1 - y]
    return tuple(map(lambda x: ''.join(x), ret))


def fuse_grid(boxes):
    sz = len(boxes[0][0])
    grid = []
    for y in range(len(boxes)*sz):
        row = []
        for x in range(len(boxes)*sz):
            row.append(boxes[y//sz][x//sz][y%sz][x%sz])
        grid.append(''.join(row))
    return grid


def get_all_rotations(box):
    ret = []
    for fl in range(2):
        for rot in range(4):
            ret.append(box)
            box = rotate(box)
        box = flip(box)
    return ret


def get_next(grid, rules):
    boxes = div_grid(grid)
    for by in range(len(boxes)):
        for bx in range(len(boxes)):
            box = boxes[by][bx]
            for key in get_all_rotations(box):
                if key in rules:
                    boxes[by][bx] = rules[key]
    return fuse_grid(boxes)


def part1():
    rules = read_input()
    grid = ['.#.',
            '..#',
            '###']
    for i in range(5):
        grid = get_next(grid, rules)
    ret = 0
    for line in grid:
        ret += line.count('#')

    return ret


def part2():
    rules = read_input()
    grid = ['.#.',
            '..#',
            '###']
    for i in range(18):
        grid = get_next(grid, rules)
    ret = 0
    for line in grid:
        ret += line.count('#')

    return ret


if __name__ == '__main__':
    print(part1(), part2())