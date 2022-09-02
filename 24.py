
def read_input():
    return [tuple(sorted(map(int, line.strip().split('/')))) for line in open('24.in')]


def strongest_path(start : int, comps : set, used : set):
    best = 0
    for c in comps:
        if c in used:
            continue
        if start not in c:
            continue
        used.add(c)
        new_start = c[0] if c[0] != start else c[1]
        best = max(best, sum(c) + strongest_path(new_start, comps, used))
        used.remove(c)

    return best

def vec_add(a, b):
    return tuple(map(sum, zip(a, b)))

def strongest_longest_path(start : int, comps : set, used : set):
    best = (0, 0)
    for c in comps:
        if c in used:
            continue
        if start not in c:
            continue
        used.add(c)
        new_start = c[0] if c[0] != start else c[1]
        best = max(best, vec_add((1, sum(c)), strongest_longest_path(new_start, comps, used)))
        used.remove(c)

    return best

def part1():
    data = read_input()
    return strongest_path(0, data, set())


def part2():
    data = read_input()
    return strongest_longest_path(0, data, set())[1]


if __name__ == '__main__':
    print(part1(), part2())