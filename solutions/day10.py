from utils.solution_base import SolutionBase
from collections import deque
from z3 import Optimize, Int, Sum, sat


class Solution(SolutionBase):
    def part1(self, data):
        diagrams = []
        buttons = []
        joltages = []

        for line in data:
            _diagram, *_button, _joltage = line.split(" ")
            _diagram = list(i == "#" for i in _diagram[1:-1])
            _button = [list(map(int, x[1:-1].split(","))) for x in _button]
            _joltage = list(map(int, _joltage[1:-1].split(",")))
            diagrams.append(_diagram)
            buttons.append(_button)
            joltages.append(_joltage)

        def solve(diagram, button):
            # BFS to find the minimal presses
            target = tuple(diagram)
            num = len(diagram)
            curr = tuple(False for _ in range(num))

            visited = {curr: 0}
            queue = deque([curr])

            while queue:
                curr = queue.popleft()
                times = visited[curr] + 1

                for btn in button:
                    next_curr = tuple(not curr[i] if i in btn else curr[i] for i in range(num))

                    if next_curr not in visited:
                        if next_curr == target:
                            return times
                        visited[next_curr] = times
                        queue.append(next_curr)

            raise ValueError("No solution found")

        c = sum(solve(diagram, button) for diagram, button in zip(diagrams, buttons))
        return c

    def part2(self, data):
        diagrams = []
        buttons = []
        joltages = []

        for line in data:
            _diagram, *_button, _joltage = line.split(" ")
            _diagram = list(i == "#" for i in _diagram[1:-1])
            _button = [list(map(int, x[1:-1].split(","))) for x in _button]
            _joltage = list(map(int, _joltage[1:-1].split(",")))
            diagrams.append(_diagram)
            buttons.append(_button)
            joltages.append(_joltage)

        def solve(joltage, button):
            # use z3 optimizer in order to get the minimal presses
            opt = Optimize()

            press_counts = [Int(f"c_{i}") for i in range(len(button))]

            # button press count must >= 0
            for count in press_counts:
                opt.add(count >= 0)

            # pick which button affects which joltage index
            for pos, jol in enumerate(joltage):
                # affects = []
                # for idx, btn in enumerate(button):
                #     if pos in btn:
                #         affects.append(press_counts[idx])
                affects = [press_counts[idx] for idx, btn in enumerate(button) if pos in btn]
                opt.add(Sum(affects) == jol)

            # minimize total presses
            opt.minimize(Sum(press_counts))

            if opt.check() == sat:
                model = opt.model()
                return sum(model[c].as_long() for c in press_counts)
            else:
                raise ValueError("No solution found")

        c = sum(solve(joltage, button) for joltage, button in zip(joltages, buttons))
        return c
