from utils.runtime import get_runtime


def get_input(test: str = None):
    with open('inputs/04') as f:
        base = test or f.read()
        l = base.splitlines()

    return l


@get_runtime
def part_1(l: list[str]):
    count = 0

    # horizontal
    for line in l:
        count += line.count('XMAS')
        count += line.count('SAMX')

    # vertical
    for i in range(len(l[0])):
        line = ''.join([x[i] for x in l])
        count += line.count('XMAS')
        count += line.count('SAMX')

    # diagonal ↙
    for d in range(len(l) + len(l[0]) - 1):
        diagonal = []
        for y in range(len(l)):
            x = d - y
            if 0 <= x < len(l[0]):
                diagonal.append(l[x][y])
        if len(diagonal) >= 4:
            diagonal_string = ''.join(diagonal)
            count += diagonal_string.count('XMAS')
            count += diagonal_string.count('SAMX')

    # diagonal ↘
    for d in range(len(l) + len(l[0]) - 1):
        diagonal = []
        if d < len(l):
            x = len(l) - d - 1
            y = 0
        else:
            x = 0
            y = d - len(l) + 1

        while x < len(l) and y < len(l[0]):
            diagonal.append(l[x][y])
            x += 1
            y += 1

        if len(diagonal) >= 4:
            diagonal_string = ''.join(diagonal)
            count += diagonal_string.count('XMAS')
            count += diagonal_string.count('SAMX')

    print(count)


@get_runtime
def part_2(l: list[str]):
    count = 0

    for x in range(len(l) - 2):
        for y in range(len(l[x]) - 2):
            if l[x][y] == l[x + 2][y] and l[x + 1][y + 1] == 'A':
                if l[x][y] == 'M':
                    if l[x][y + 2] == l[x + 2][y + 2] == 'S':
                        count += 1
                elif l[x][y] == 'S':
                    if l[x][y + 2] == l[x + 2][y + 2] == 'M':
                        count += 1
            elif l[x][y] == l[x][y + 2] and l[x + 1][y + 1] == 'A':
                if l[x][y] == 'M':
                    if l[x + 2][y] == l[x + 2][y + 2] == 'S':
                        count += 1
                elif l[x][y] == 'S':
                    if l[x + 2][y] == l[x + 2][y + 2] == 'M':
                        count += 1

    print(count)


part_1(get_input())
part_2(get_input())
