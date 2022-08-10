
def read_input():
    return open('09.in').read().strip()

def score(s):
    i = 0
    lvl = 1
    tot = 0
    garb = False
    while i < len(s):
        if s[i] == '!':
            i += 2
            continue
        if garb:
            if s[i] == '>':
                garb = False
            i += 1
            continue
        if s[i] == '{':
            tot += lvl
            lvl += 1
            i += 1
        elif s[i] == '}':
            lvl -= 1
            i += 1
        elif s[i] == '<':
            garb = True
            i += 1
        else:
            i += 1
    return tot


def score_garb(s):
    i = 0
    lvl = 1
    tot = 0
    garb = False
    while i < len(s):
        if s[i] == '!':
            i += 2
            continue
        if garb:
            if s[i] == '>':
                garb = False
            else:
                tot += 1
            i += 1
            continue
        if s[i] == '{':
            lvl += 1
            i += 1
        elif s[i] == '}':
            lvl -= 1
            i += 1
        elif s[i] == '<':
            garb = True
            i += 1
        else:
            i += 1
    return tot

def part1():
    data = read_input()
    return score(data)


def part2():
    data = read_input()
    return score_garb(data)


if __name__ == '__main__':
    print(part1(), part2())