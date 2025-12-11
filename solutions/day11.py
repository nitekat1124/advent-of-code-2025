from utils.solution_base import SolutionBase


class Solution(SolutionBase):
    def part1(self, data):
        routes = {}
        for line in data:
            _name, _outputs = line.split(": ")
            _outputs = _outputs.split()
            routes[_name] = _outputs

        count = self.count_paths(routes, "you", "out")
        return count

    def part2(self, data):
        routes = {}
        for line in data:
            _name, _outputs = line.split(": ")
            _outputs = _outputs.split()
            routes[_name] = _outputs

        count1a = self.count_paths(routes, "svr", "dac")
        count1b = self.count_paths(routes, "dac", "fft")
        count1c = self.count_paths(routes, "fft", "out")
        count1 = count1a * count1b * count1c

        count2a = self.count_paths(routes, "svr", "fft")
        count2b = self.count_paths(routes, "fft", "dac")
        count2c = self.count_paths(routes, "dac", "out")
        count2 = count2a * count2b * count2c

        return count1 + count2

    def count_paths(self, routes, start, end):
        if start not in routes:
            return 0

        # store how many paths from curr(dict key) to end
        cache = {}

        def dfs(curr, end):
            if curr == end:
                return 1
            if curr in cache:
                return cache[curr]

            count = sum(dfs(_next, end) for _next in routes.get(curr, []))
            cache[curr] = count
            return count

        return dfs(start, end)
