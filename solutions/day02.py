from utils.solution_base import SolutionBase


class Solution(SolutionBase):
    def part1(self, data):
        id_ranges = data[0].split(",")
        result = 0

        for _range in id_ranges:
            _start, _end = map(int, _range.split("-"))
            for _id in range(_start, _end + 1):
                _id_str = str(_id)
                _len = len(_id_str)
                if _len % 2 != 0:
                    continue
                if _id_str[: _len // 2] * 2 == _id_str:
                    result += _id
        return result

    def part2(self, data):
        id_ranges = data[0].split(",")
        result = 0

        for _range in id_ranges:
            _start, _end = map(int, _range.split("-"))
            for _id in range(_start, _end + 1):
                _id_str = str(_id)
                _len = len(_id_str)
                for c in range(1, _len // 2 + 1):
                    if _len % c != 0:
                        continue
                    if _id_str[:c] * (_len // c) == _id_str:
                        result += _id
                        break
        return result
