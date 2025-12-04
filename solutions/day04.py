from utils.solution_base import SolutionBase


class Solution(SolutionBase):
    def make_a_map(self, data):
        w = len(data[0]) + 2
        _map = [["."] * w] + [["."] + list(row) + ["."] for row in data] + [["."] * w]
        return _map, w, len(_map)

    def find_accessible(self, _map, w, h):
        _dirs = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
        pos = [(i, j) for i in range(1, h) for j in range(1, w) if _map[i][j] == "@" and sum(1 for _dir in _dirs if _map[i + _dir[0]][j + _dir[1]] == "@") < 4]
        return pos

    def part1(self, data):
        _map, w, h = self.make_a_map(data)
        _pos = self.find_accessible(_map, w, h)
        return len(_pos)

    def part2(self, data):
        _map, w, h = self.make_a_map(data)
        count = 0
        _pos = self.find_accessible(_map, w, h)
        while (c := len(_pos)) > 0:
            count += c
            for y, x in _pos:
                _map[y][x] = "."
            _pos = self.find_accessible(_map, w, h)
        return count
