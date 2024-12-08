from collections import defaultdict
from itertools import combinations
from operator import add, sub

from utils.runtime import get_runtime


def get_input(test: str = None):
    with open('inputs/08') as f:
        base = test or f.read()
        l = [list(line) for line in base.splitlines()]

    nodes = defaultdict(list)

    for x, row in enumerate(l):
        for y, elem in enumerate(row):
            if elem != '.':
                nodes[elem].append((x, y))

    return nodes, len(l)


@get_runtime
def part_1(nodes: defaultdict[str, list[tuple[int, int]]], grid_length: int):
    antinodes = set()

    for coordinates in nodes.values():
        for c1, c2 in combinations(coordinates, 2):
            diff = tuple(map(sub, c1, c2))

            a1 = tuple(map(add, c1, diff))
            if all(0 <= i < grid_length for i in a1):
                antinodes.add(a1)

            a2 = tuple(map(sub, c2, diff))
            if all(0 <= i < grid_length for i in a2):
                antinodes.add(a2)

    print(len(antinodes))


@get_runtime
def part_2(nodes: defaultdict[str, list[tuple[int, int]]], grid_length: int):
    antinodes = set()

    for coordinates in nodes.values():
        for c1, c2 in combinations(coordinates, 2):
            antinodes.add(c1)
            antinodes.add(c2)

            diff = tuple(map(sub, c1, c2))

            a1 = tuple(map(add, c1, diff))
            while all(0 <= i < grid_length for i in a1):
                antinodes.add(a1)
                a1 = tuple(map(add, a1, diff))

            a2 = tuple(map(sub, c2, diff))
            while all(0 <= i < grid_length for i in a2):
                antinodes.add(a2)
                a2 = tuple(map(sub, a2, diff))

    print(len(antinodes))


part_1(*get_input())
part_2(*get_input())
