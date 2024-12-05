from copy import deepcopy
from itertools import pairwise

from utils.runtime import get_runtime


def get_input(test: str = None):
    with open('inputs/05') as f:
        base = test or f.read()
        rules, updates = base.split('\n\n')

    rules_pairs = []
    for rule in rules.splitlines():
        x, y = map(int, rule.split('|'))
        rules_pairs.append((x, y))

    updates_list = [
        list(map(int, update.split(','))) for update in updates.splitlines()
    ]

    return rules_pairs, updates_list


@get_runtime
def part_1(rules: list[tuple[int, int]], updates: list[list[int]]):
    result = 0

    for update in updates:
        for i, j in pairwise(update):
            if j in [x[0] for x in rules]:
                if i in [x[1] for x in rules if x[0] == j]:
                    break
        else:
            result += update[len(update) // 2]

    print(result)


@get_runtime
def part_2(rules: list[tuple[int, int]], updates: list[list[int]]):
    result = 0

    for update in updates:
        correct = True
        while True:
            c = 0
            for i, j in pairwise(update):
                if j in [x[0] for x in rules]:
                    if i in [x[1] for x in rules if x[0] == j]:
                        correct = False
                        new_update = deepcopy(update)
                        new_update[update.index(i)] = j
                        new_update[update.index(j)] = i
                        update = new_update
                        c += 1
            if correct:
                break
            if c == 0:
                result += update[len(update) // 2]
                break

    print(result)


part_1(*get_input())
part_2(*get_input())
