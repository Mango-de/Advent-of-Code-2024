from operator import add

from utils.runtime import get_runtime


def get_input(test: str = None):
    with open('inputs/10') as f:
        base = test or f.read()
        l = [[int(x) for x in line] for line in base.splitlines()]

    return l


def get_endpoints(l: list[list[int]], trailhead: tuple[int, int]):
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    endpoints = []
    to_go = [trailhead]

    while len(to_go) > 0:
        x, y = to_go.pop()
        current = l[x][y]
        target = current + 1

        for direction in directions:
            nx, ny = map(add, (x, y), direction)
            if 0 <= nx < len(l) and 0 <= ny < len(l[nx]) and l[nx][ny] == target:
                if target == 9:
                    endpoints.append((nx, ny))
                else:
                    to_go.append((nx, ny))

    return endpoints


@get_runtime
def part_1(l: list[list[int]]):
    result = 0

    for x, i in enumerate(l):
        for y, j in enumerate(i):
            if j == 0:
                result += len(set(get_endpoints(l, (x, y))))

    print(result)


@get_runtime
def part_2(l: list[list[int]]):
    result = 0

    for x, i in enumerate(l):
        for y, j in enumerate(i):
            if j == 0:
                result += len(get_endpoints(l, (x, y)))

    print(result)


part_1(get_input())
part_2(get_input())
