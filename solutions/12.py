from operator import add

from utils.runtime import get_runtime

directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def get_input(test: str = None):
    with open('inputs/12') as f:
        base = test or f.read()
        l = list(map(list, base.splitlines()))

    return l


def get_region(l: list[list[str]], x: int, y: int) -> list[tuple[int, int]]:
    plots = [(x, y)]
    to_go = [(x, y)]

    while len(to_go) > 0:
        x, y = to_go.pop()
        current = l[x][y]

        for direction in directions:
            nx, ny = map(add, (x, y), direction)

            if 0 <= nx < len(l) and 0 <= ny < len(l[nx]) and l[nx][ny] == current:
                if (nx, ny) not in plots:
                    plots.append((nx, ny))
                    to_go.append((nx, ny))

    return plots


def get_regions(l: list[list[str]]) -> list[list[tuple[int, int]]]:
    regions = []

    for x in range(len(l)):
        for y in range(len(l[x])):
            if (x, y) not in [c for rg in regions for c in rg]:
                region = get_region(l, x, y)
                regions.append(region)

    return regions


def get_perimeter(region: list[tuple[int, int]]) -> int:
    perimeter = 0

    for x, y in region:
        for direction in directions:
            nx, ny = map(add, (x, y), direction)

            if (nx, ny) not in region:
                perimeter += 1

    return perimeter


def get_sides(region: list[tuple[int, int]]) -> int:
    sides = 0
    fences = []

    for x, y in sorted(region, key=lambda i: (i[0], i[1])):
        for direction in directions:
            nx, ny = map(add, (x, y), direction)

            if (nx, ny) not in region:
                fences.append((nx, ny, directions.index(direction)))

                for dx, dy in [
                    directions[(directions.index(direction) + i) % 4] for i in [1, 3]
                ]:
                    sx, sy = map(add, (nx, ny), (dx, dy))

                    if (sx, sy, directions.index(direction)) in fences:
                        break
                else:
                    sides += 1

    return sides


@get_runtime
def part_1(l: list[list[str]]):
    print(sum([len(reg) * get_perimeter(reg) for reg in get_regions(l)]))


@get_runtime
def part_2(l: list[list[str]]):
    print(sum([len(reg) * get_sides(reg) for reg in get_regions(l)]))


part_1(get_input())
part_2(get_input())
