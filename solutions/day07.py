from utils.solution_base import SolutionBase
from collections import defaultdict


class Solution(SolutionBase):
    def parse_data(self, data):
        _map = []
        st = None
        for y, line in enumerate(data):
            row = list(line)
            if y == 0 and st is None:
                for x, c in enumerate(row):
                    if c == "S":
                        st = (y, x)
            _map.append(row)
        return _map, st

    def part1(self, data):
        _map, (y, x) = self.parse_data(data)

        beams = {x}
        splitters = 0

        while True:
            if y > len(_map) - 2:
                break

            y += 1
            next_beams = set()

            for x in beams:
                if _map[y][x] == "^":
                    next_beams.add(x - 1)
                    next_beams.add(x + 1)
                    splitters += 1
                else:
                    next_beams.add(x)
            beams = next_beams
        return splitters

    def part2(self, data):
        _map, (y, x) = self.parse_data(data)

        beams = defaultdict(int)
        beams[x] = 1

        while True:
            if y > len(_map) - 2:
                break

            y += 1
            next_beams = defaultdict(int)

            for x in beams:
                n = beams[x]
                if _map[y][x] == "^":
                    next_beams[x - 1] += n
                    next_beams[x + 1] += n
                else:
                    next_beams[x] += n
            beams = next_beams

        return sum(beams.values())
