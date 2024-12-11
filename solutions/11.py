import math

from utils.runtime import get_runtime


def get_input(test: str = None):
    with open('inputs/11') as f:
        base = test or f.read()
        l = list(map(int, base.split()))

    return l


def solve(stones: list[int], blinks: int):
    cache = {}

    def blink(stone: int, blinks: int):
        if blinks == 0:
            return 1

        if (stone, blinks) in cache:
            return cache[(stone, blinks)]

        if stone == 0:
            size = blink(1, blinks - 1)
        elif (digit_count := (math.floor(math.log(stone, 10)) + 1)) % 2 == 0:
            left = stone // 10 ** (digit_count // 2)
            right = stone % 10 ** (digit_count // 2)
            size = blink(left, blinks - 1) + blink(right, blinks - 1)
        else:
            size = blink(stone * 2024, blinks - 1)

        if (stone, blinks) not in cache:
            cache[(stone, blinks)] = size

        return size

    return sum(blink(stone, blinks) for stone in stones)


@get_runtime
def part_1(l: list[int]):
    print(solve(l, 25))


@get_runtime
def part_2(l: list[int]):
    print(solve(l, 75))


part_1(get_input())
part_2(get_input())
