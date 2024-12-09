from utils.runtime import get_runtime


def get_input(test: str = None):
    with open('inputs/09') as f:
        base = test or f.read()

    return base


@get_runtime
def part_1(l: str):
    blocks = []

    for c, block in enumerate(l):
        blocks.extend(((str(c // 2) if c % 2 == 0 else '.') for _ in range(int(block))))

    while '.' in blocks:
        elem = blocks.pop()
        if elem != '.':
            blocks[blocks.index('.')] = elem

    print(sum(i * int(id) for i, id in enumerate(blocks)))


@get_runtime
def part_2(l: str):  # takes a lot of time to compute, but it works :)
    blocks = []

    for c, block in enumerate(l):
        bl = []
        bl.extend((str(c // 2) if c % 2 == 0 else '.') for _ in range(int(block)))
        if len(bl) > 0:
            blocks.append(bl)

    for c in range(len(blocks) - 1, 0, -1):
        block = blocks[c]
        if block[-1] == '.':
            continue

        for dots in [b for b in blocks if b[-1] == '.']:
            if len([d for d in dots if d == '.']) >= len(block) and blocks.index(
                dots
            ) < blocks.index(block):
                no_dots = len([x for x in dots if x != '.'])
                for j, file_fragment in enumerate(block):
                    dots[j + no_dots] = file_fragment

                blocks[blocks.index(dots)] = dots
                blocks.reverse()
                blocks[blocks.index(block)] = ['.'] * len(block)
                blocks.reverse()

                break

    print(
        sum(
            (i * int(id) if id != '.' else 0)
            for i, id in enumerate([b for bl in blocks for b in bl])
        )
    )


part_1(get_input())
part_2(get_input())
