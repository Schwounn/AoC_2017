
def read_input():
    return int(open('03.in').read())


def part1():
    data = read_input()
    circle = 1
    while (circle + 2)**2 < data:
        circle += 2
    side_length = circle + 2
    i = data - circle**2
    while i - (circle + 1) >= 0:
        i -= circle + 1
    to_mid = abs(side_length // 2 - i)
    return circle // 2 + 1 + to_mid


def coords(data):
    if data == 1:
        return 0, 0
    circle = 1
    while (circle + 2) ** 2 < data:
        circle += 2
    side_length = circle + 2
    side = 0
    i = data - circle ** 2
    while i - (circle + 1) > 0:
        side += 1
        i -= circle + 1
    to_mid = side_length // 2 - i
    from_side = circle // 2 + 1
    if side == 0:
        return from_side, -to_mid
    elif side == 1:
        return to_mid, from_side
    elif side == 2:
        return -from_side, to_mid
    else:
        return -to_mid, -from_side


def get_neighbors(x, y):
    ret = []
    for dy in [-1, 0, 1]:
        for dx in [-1, 0, 1]:
            if dy != 0 or dx != 0:
                ret.append((x + dx, y + dy))
    return ret


def part2():
    data = read_input()
    coord_to_val = {(0, 0): 1}
    i = 2
    while True:
        cor = coords(i)
        val = sum([coord_to_val[c] for c in get_neighbors(*cor) if c in coord_to_val])
        if val > data:
            return val
        coord_to_val[cor] = val
        i += 1

if __name__ == '__main__':
    print(part1(), part2())