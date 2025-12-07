from utils.solution_base import SolutionBase


class Solution(SolutionBase):
    def parse_data(self, data):
        _map = []
        st = None
        for y, line in enumerate(data):
            row = list(line)
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

        beams = {x: 1}

        while True:
            if y > len(_map) - 2:
                break

            y += 1
            next_beams = {}

            for x in beams:
                n = beams[x]
                if _map[y][x] == "^":
                    next_beams[x - 1] = next_beams.get(x - 1, 0) + n
                    next_beams[x + 1] = next_beams.get(x + 1, 0) + n
                else:
                    next_beams[x] = next_beams.get(x, 0) + n
            beams = next_beams

        return sum(beams.values())
