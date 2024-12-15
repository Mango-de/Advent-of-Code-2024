from copy import deepcopy
from operator import add, sub

from utils.runtime import get_runtime

directions = {'^': (-1, 0), '>': (0, 1), 'v': (1, 0), '<': (0, -1)}


def get_input(test: str = None):
    with open('inputs/15') as f:
        base = test or f.read()
        warehouse_map, movements = base.split('\n\n')

    return [list(line) for line in warehouse_map.splitlines()], list(
        ''.join(movements.splitlines())
    )


@get_runtime
def part_1(l: list[list[str]], movements: list[str]):
    for x in range(len(l)):
        for y in range(len(l[x])):
            if l[x][y] == '@':
                starting_position = (x, y)
                break

    def move(x: int, y: int, direction: tuple[int, int]):
        nx, ny = map(add, (x, y), direction)

        if l[nx][ny] == '.':
            l[x][y] = '.'
            l[nx][ny] = '@'

            return nx, ny

        elif l[nx][ny] == 'O':
            bx, by = map(add, (nx, ny), direction)

            while l[bx][by] == 'O':
                bx, by = map(add, (bx, by), direction)

            if l[bx][by] == '.':
                l[bx][by] = 'O'
                l[x][y] = '.'
                l[nx][ny] = '@'

                return nx, ny

        return x, y  # robot did not move

    x, y = starting_position

    for movement in movements:
        x, y = move(x, y, directions[movement])

    result = 0

    for i in range(len(l)):
        for j in range(len(l[i])):
            if l[i][j] == 'O':
                result += 100 * i + j

    print(result)


@get_runtime
def part_2(l: list[list[str]], movements: list[str]):
    new_map = []

    for x, i in enumerate(l):
        new_map.append([])
        for j in i:
            if j == '#':
                new_map[x].extend('##')
            elif j == '.':
                new_map[x].extend('..')
            elif j == 'O':
                new_map[x].extend('[]')
            elif j == '@':
                new_map[x].extend('@.')

    l = new_map

    for x in range(len(l)):
        for y in range(len(l[x])):
            if l[x][y] == '@':
                starting_position = (x, y)
                break

    def move(l: list[list[str]], x: int, y: int, direction: tuple[int, int]):
        nx, ny = map(add, (x, y), direction)

        if l[nx][ny] == '.':
            l[x][y] = '.'
            l[nx][ny] = '@'

            return l, nx, ny

        elif l[nx][ny] in '[]':
            if direction[0] == 0:  # left or right movement
                bx, by = map(add, (nx, ny), direction)

                while l[bx][by] in '[]':
                    bx, by = map(add, (bx, by), direction)

                if l[bx][by] == '.':
                    i = 0

                    if direction[1] == 1:
                        i += 1

                    while (bx, by) != (nx, ny):
                        l[bx][by] = '[]'[i]
                        bx, by = map(sub, (bx, by), (direction))
                        i = (i + 1) % 2

                    l[x][y] = '.'
                    l[nx][ny] = '@'

                    return l, nx, ny

            elif direction[1] == 0:  # up or down movement
                to_move = []

                def add_box(cx, cy):
                    if (cx, cy) not in to_move:
                        to_move.append((cx, cy))

                    ncx1, ncy1 = map(add, (cx, cy), direction)

                    if l[cx][cy] == '[':
                        if (cx, cy + 1) not in to_move:
                            to_move.append((cx, cy + 1))

                        ncx2, ncy2 = map(add, (cx, cy + 1), direction)

                    elif l[cx][cy] == ']':
                        if (cx, cy - 1) not in to_move:
                            to_move.append((cx, cy - 1))

                        ncx2, ncy2 = map(add, (cx, cy - 1), direction)

                    if l[ncx1][ncy1] in '[]':
                        add_box(ncx1, ncy1)

                    if l[ncx2][ncy2] in '[]':
                        add_box(ncx2, ncy2)

                add_box(nx, ny)
                update_map = deepcopy(l)

                # ascending when pushing down, descending when pushing up
                to_move.sort(key=lambda t: t[0], reverse=direction[0] == -1)

                while len(to_move) > 0:
                    cx, cy = to_move.pop()
                    ncx, ncy = map(add, (cx, cy), direction)

                    if l[ncx][ncy] != '#':
                        update_map[ncx][ncy] = update_map[cx][cy]
                        update_map[cx][cy] = '.'

                    else:
                        break

                else:  # ignore changes in case a box could not be moved
                    update_map[x][y] = '.'
                    update_map[nx][ny] = '@'

                    return update_map, nx, ny

        return l, x, y  # robot did not move

    x, y = starting_position

    for movement in movements:
        l, x, y = move(l, x, y, directions[movement])

    result = 0

    for i in range(len(l)):
        for j in range(len(l[i])):
            if l[i][j] == '[':
                result += 100 * i + j

    print(result)


part_1(*get_input())
part_2(*get_input())
