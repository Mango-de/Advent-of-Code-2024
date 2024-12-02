from itertools import pairwise

from utils.runtime import get_runtime


def get_input(test: str = None):
    with open('inputs/02') as f:
        base = test or f.read()
        l = base.splitlines()

    return [list(map(int, line.split())) for line in l]


@get_runtime
def part_1(l: list[list[int]]):
    safe = 0

    for report in l:
        if sorted(report) == report or sorted(report, reverse=True) == report:
            for i, j in pairwise(sorted(report)):
                if not 1 <= j - i <= 3:
                    break
            else:
                safe += 1

    print(safe)


@get_runtime
def part_2(l: list[list[int]]):
    safe = 0

    for report in l:
        for k in range(len(report)):
            rep = report[:k] + report[k + 1 :]
            if sorted(rep) == rep or sorted(rep, reverse=True) == rep:
                for i, j in pairwise(sorted(rep)):
                    if not 1 <= j - i <= 3:
                        break
                else:
                    safe += 1
                    break

    print(safe)


part_1(get_input())
part_2(get_input())
