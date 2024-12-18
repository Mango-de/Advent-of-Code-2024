import re

from utils.runtime import get_runtime


def get_input(test: str = None):
    with open('inputs/03') as f:
        base = test or f.read()
        l = base.splitlines()

    return l


@get_runtime
def part_1(l: list[str]):
    result = 0

    for line in l:
        valid = re.findall(r'mul\((\d+),(\d+)\)', line)

        for x, y in valid:
            result += int(x) * int(y)

    print(result)


@get_runtime
def part_2(l: list[str]):
    result = 0
    text = ''.join(l)

    while True:
        i = text.find("don't()")
        valid = re.findall(r'mul\((\d+),(\d+)\)', text[:i])

        for x, y in valid:
            result += int(x) * int(y)

        text = text[i:]
        j = text.find("do()")
        text = text[j + 4 :]

        if j == -1:
            break

    print(result)


part_1(get_input())
part_2(get_input())
