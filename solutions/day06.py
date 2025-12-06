from utils.solution_base import SolutionBase
import math


class Solution(SolutionBase):
    def part1(self, data):
        opes = data[-1].split()
        totals = [int(ope == "*") for ope in opes]

        for line in data[:-1]:
            nums = map(int, line.split())
            for i, num in enumerate(nums):
                if opes[i] == "*":
                    totals[i] *= num
                else:
                    totals[i] += num
        return sum(totals)

    def part2(self, data):
        # should use raw data instead of stripped data in part 2
        self.check_is_raw()

        opes = []
        problems = []
        curr = []

        # rotate the data 90 degrees counter-clockwise
        for line in zip(*[line[::-1] for line in data]):
            if all(c == " " for c in line):
                continue
            curr.append(int("".join(line[:-1])))
            if line[-1] != " ":
                opes.append(line[-1])
                problems.append(curr)
                curr = []

        totals = [[math.prod, sum][ope == "+"](problem) for ope, problem in zip(opes, problems)]
        return sum(totals)
