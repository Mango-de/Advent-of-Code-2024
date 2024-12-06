from itertools import cycle
from operator import add

from utils.runtime import get_runtime


def get_input(test: str = None):
    with open('inputs/06') as f:
        base = test or f.read()
        l = [list(x) for x in base.splitlines()]

    return l


def get_visited_positions(l: list[list[str]]) -> list[tuple[int, int]]:
    directions = cycle([(-1, 0), (0, 1), (1, 0), (0, -1)])

    for x in range(len(l)):
        for y in range(len(l[x])):
            if l[x][y] == '^':
                starting_pos = x, y
                break

    current_direction = next(directions)
    visited = [starting_pos]
    current_pos = starting_pos

    while True:
        nx, ny = tuple(map(add, current_pos, current_direction))

        if 0 <= nx < len(l) and 0 <= ny < len(l[0]):
            if l[nx][ny] == '#':
                current_direction = next(directions)
            else:
                current_pos = nx, ny
                visited.append((nx, ny))
        else:
            break

    return list(set(visited))


@get_runtime
def part_1(l: list[list[str]]):
    print(len(get_visited_positions(l)))


def check_path(grid: list[list[str]], starting_pos: tuple[int, int]):
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    current_direction = 0
    visited = [(*starting_pos, current_direction)]
    current_pos = starting_pos

    while True:
        nx, ny = tuple(map(add, current_pos, directions[current_direction % 4]))

        if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]):
            if grid[nx][ny] == '#':
                current_direction += 1
            else:
                current_pos = nx, ny

                if (nx, ny, current_direction % 4) in visited:
                    return True

                visited.append((nx, ny, current_direction % 4))
        else:
            break

    return False


@get_runtime
def part_2(l: list[list[str]]):  # takes some time to compute, but it works :)
    for x in range(len(l)):
        for y in range(len(l[x])):
            if l[x][y] == '^':
                starting_pos = x, y
                break

    count = 0
    visited = get_visited_positions(l)

    for x in range(len(l)):
        for y in range(len(l[x])):
            if (x, y) != starting_pos and l[x][y] == '.' and (x, y) in visited:
                l[x][y] = '#'

                if check_path(l, starting_pos):
                    count += 1

                l[x][y] = '.'

    print(count)


part_1(get_input())
part_2(get_input())
