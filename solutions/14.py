import math
import re
from collections import defaultdict

from PIL import Image, ImageDraw, ImageFont

from utils.runtime import get_runtime


def get_input(test: str = None):
    with open('inputs/14') as f:
        base = test or f.read()
        l = [[int(n) for n in re.findall(r'-?\d+', line)] for line in base.splitlines()]

    return l


@get_runtime
def part_1(l: list[list[int]], width: int, height: int):
    result = []

    for x, y, dx, dy in l:
        for _ in range(100):
            x = (x + dx) % width
            y = (y + dy) % height
        result.append((y, x))

    quadrants = defaultdict(int)

    for i in range(width):
        for j in range(height):
            if i < width // 2 and j < height // 2:
                for _ in range(result.count((j, i))):
                    quadrants[0] += 1
            elif width // 2 < i and j < height // 2:
                for _ in range(result.count((j, i))):
                    quadrants[1] += 1
            elif i < width // 2 and height // 2 < j:
                for _ in range(result.count((j, i))):
                    quadrants[2] += 1
            elif width // 2 < i and height // 2 < j:
                for _ in range(result.count((j, i))):
                    quadrants[3] += 1

    print(math.prod(quadrants.values()))


@get_runtime
def part_2(l: list[list[int]], width: int, height: int):
    # use a font that uses the same width for each character
    font = ImageFont.truetype('FiraCodeNerdFont-Regular.ttf', size=8)

    # 10000 loops may not be enough for every puzzle input, but it was for me
    for c in range(10000):
        res = []

        for e, (x, y, dx, dy) in enumerate(l):
            x = (x + dx) % width
            y = (y + dy) % height
            res.append((y, x))
            l[e] = [x, y, dx, dy]

        text = ''

        for i in range(height):
            for j in range(width):
                if (i, j) in res:
                    text += '#'
                else:
                    text += ' '
            text += '\n'

        img = Image.new(
            'RGB',
            (width * 6, height * 9),
        )
        draw = ImageDraw.Draw(img)
        draw.text(
            (0, 0),
            text,
            spacing=0,
            font=font,
        )

        # search through every single picture until you find the right one :)
        img.save(f'day 14 part 2 pictures/{c + 1}.jpg')


part_1(get_input(), 101, 103)
part_2(get_input(), 101, 103)
