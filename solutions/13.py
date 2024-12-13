import re

from sympy import Matrix, solve_linear_system
from sympy.abc import x, y
from sympy.core.numbers import Integer

from utils.runtime import get_runtime


def get_input(test: str = None):
    with open('inputs/13') as f:
        base = test or f.read()
        l = base.split('\n\n')

    return l


@get_runtime
def part_1(l: list[str]):
    result = 0

    for claw_machine in l:
        xa, ya, xb, yb, dx, dy = map(int, re.findall(r'\d+', claw_machine))

        found = False
        for i in range(1, 101):
            if found:
                break

            for j in range(1, 101):
                if i * xa + j * xb == dx and i * ya + j * yb == dy:
                    result += 3 * i + j
                    found = True

                    break

    print(result)


@get_runtime
def part_2(l: list[str]):
    result = 0

    for claw_machine in l:
        xa, ya, xb, yb, dx, dy = map(int, re.findall(r'\d+', claw_machine))

        system = Matrix(
            ((xa, xb, dx + 10_000_000_000_000), (ya, yb, dy + 10_000_000_000_000))
        )
        solutions = solve_linear_system(system, x, y)

        if isinstance(solutions[x], Integer) and isinstance(solutions[y], Integer):
            result += 3 * int(solutions[x]) + int(solutions[y])

    print(result)


part_1(get_input())
part_2(get_input())
