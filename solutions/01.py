from utils.runtime import get_runtime


def get_input(test: str = None):
    with open('inputs/01') as f:
        base = test or f.read()
        l = base.splitlines()

    l1 = []
    l2 = []
    for line in l:
        p1, p2 = map(int, line.split())
        l1.append(p1)
        l2.append(p2)
    return sorted(l1), sorted(l2)


@get_runtime
def part_1(l1: list[int], l2: list[int]):
    s = 0

    for x1, x2 in zip(l1, l2):
        s += abs(x2 - x1)

    print(s)


@get_runtime
def part_2(l1: list[int], l2: list[int]):
    s = 0

    for x in l1:
        s += x * l2.count(x)

    print(s)


part_1(*get_input())
part_2(*get_input())
