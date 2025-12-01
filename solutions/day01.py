from utils.solution_base import SolutionBase


class Solution(SolutionBase):
    def part1(self, data):
        pointing = 50
        zero_counter = 0

        for line in data:
            turn, dist = line[0], int(line[1:])
            sign = "LCR".index(turn) - 1

            r = dist % 100
            pointing = (pointing + sign * r + 100) % 100
            if pointing == 0:
                zero_counter += 1

        return zero_counter

    def part2(self, data):
        pointing = 50
        zero_counter = 0

        for line in data:
            turn, dist = line[0], int(line[1:])
            sign = "LCR".index(turn) - 1

            c = dist // 100
            zero_counter += c

            r = dist % 100
            if r > 0:
                new_pointing = pointing + sign * r
                if (sign > 0 and new_pointing >= 100) or (sign < 0 and new_pointing < 1 and pointing > 0):
                    zero_counter += 1
                pointing = (new_pointing + 100) % 100

        return zero_counter
