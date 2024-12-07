from itertools import product

from utils.runtime import get_runtime


def get_input(test: str = None):
    with open('inputs/07') as f:
        base = test or f.read()
        l = base.splitlines()

    return [
        (int(value), tuple(map(int, operators.split())))
        for value, operators in [line.split(': ') for line in l]
    ]


@get_runtime
def part_1(l: list[tuple[int, tuple[int, ...]]]):
    calibration_result = 0

    for result, operators in l:
        for operands in product(*[('+', '*') for _ in range(len(operators) - 1)]):
            current = operators[0]
            for c, x in enumerate(operators[1:]):
                if operands[c] == '+':
                    current += x
                else:
                    current *= x

            if current == result:
                calibration_result += current
                break

    print(calibration_result)


@get_runtime
def part_2(l: list[tuple[int, tuple[int, ...]]]):
    calibration_result = 0

    for result, operators in l:
        for operands in product(*[('+', '*', '||') for _ in range(len(operators) - 1)]):
            current = operators[0]
            for c, x in enumerate(operators[1:]):
                if operands[c] == '+':
                    current += x
                elif operands[c] == '*':
                    current *= x
                else:
                    current = current * 10 ** len(str(x)) + x

            if current == result:
                calibration_result += current
                break

    print(calibration_result)


part_1(get_input())
part_2(get_input())
