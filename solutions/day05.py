from utils.solution_base import SolutionBase


class Solution(SolutionBase):
    def part1(self, data):
        blank = data.index("")
        ranges = [[*map(int, i.split("-"))] for i in data[:blank]]
        ids = [*map(int, data[blank + 1 :])]

        total = 0
        for _id in ids:
            for x, y in ranges:
                if x <= _id <= y + 1:
                    total += 1
                    break
        return total

    def part2(self, data):
        blank = data.index("")
        ranges = sorted([*map(int, i.split("-"))] for i in data[:blank])

        merged = [ranges[0]]
        for x2, y2 in ranges[1:]:
            x1, y1 = merged[-1]
            if x2 > y1:
                merged.append([x2, y2])
            else:
                merged[-1][1] = max(y1, y2)

        total = sum(y - x + 1 for x, y in merged)
        return total
