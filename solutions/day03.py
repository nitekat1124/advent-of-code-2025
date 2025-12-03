from utils.solution_base import SolutionBase


class Solution(SolutionBase):
    def part1(self, data):
        joltage = 0
        for line in data:
            nums = [*map(int, line)]
            n = 0

            for i, x in enumerate(nums[:-1]):
                for j, y in enumerate(nums[i + 1 :]):
                    t = 10 * x + y
                    if t > n:
                        n = t
            joltage += n
        return joltage

    def part2(self, data):
        joltage = 0
        for line in data:
            nums = [*map(int, line)]
            n = 0

            for i in range(11, -1, -1):
                temp = nums[: len(nums) - i]
                _max = max(temp)
                _idx = temp.index(_max)
                nums = nums[_idx + 1 :]
                n = n * 10 + _max

            joltage += n
        return joltage
