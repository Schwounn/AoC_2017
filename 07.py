from collections import Counter

def read_input():
    raw = [line.strip() for line in open('07.in')]
    weights = {}
    tree = {}
    for line in raw:
        ls = line.split('->')
        lh = ls[0].split()
        node = lh[0]
        w = int(lh[1][1:-1])
        weights[node] = w
        if len(ls) > 1:
            children = list(map(str.strip, ls[1].split(',')))
            tree[node] = children
    return weights, tree


def part1():
    weights, tree = read_input()
    for node in weights:
        for n in tree:
            if node in tree[n]:
                break
        else:
            return node


def get_balanced_weight(root, weights, tree):
    if root not in tree:
        return None, weights[root]
    w = 0
    ret = None
    sub_w = []
    for child in tree[root]:
        unbalanced, sw = get_balanced_weight(child, weights, tree)
        sub_w.append((sw, child))
        if unbalanced:
            ret = unbalanced
        w += sw
    if not ret:
        counter = Counter(map(lambda x: x[0], sub_w))
        odd_one = min(sub_w, key=lambda x:counter.get(x[0]))
        if counter.get(odd_one[0]) == 1:
            unbalanced_weight = odd_one[0]
            wanted_weight = max(sub_w, key=lambda x:counter.get(x[0]))[0]
            ret = wanted_weight - unbalanced_weight + weights[odd_one[1]]
    return ret, w + weights[root]


def part2():
    root = part1()
    weights, tree = read_input()
    unbalanced, total_w = get_balanced_weight(root, weights, tree)
    return unbalanced

if __name__ == '__main__':
    print(part1(), part2())