from utils.solution_base import SolutionBase
from itertools import combinations


class Solution(SolutionBase):
    def part1(self, data):
        pos = [tuple(map(int, line.split(","))) for line in data]

        area = -1
        for a, b in combinations(pos, 2):
            x1, y1 = a
            x2, y2 = b

            w = abs(x1 - x2) + 1
            h = abs(y1 - y2) + 1
            area = max(area, w * h)
        return area

    def part2(self, data):
        pos = [tuple(map(int, line.split(","))) for line in data]
        edges = [(pos[i], pos[(i + 1) % len(pos)]) for i in range(len(pos))]

        def edge_is_intersect(side, edge):
            a, b = side
            c, d = edge

            # both vertical or both horizontal
            if (a[0] == b[0] and c[0] == d[0]) or (a[1] == b[1] and c[1] == d[1]):
                return False

            if a[0] == b[0]:  # side is vertical
                # if c[0] == a[0] or d[0] == a[0]:  # T shape not count
                #     return False
                # if (c[0] < a[0] and d[0] < a[0]) or (c[0] > a[0] and d[0] > a[0]):  # both points of edge is on the same side
                #     return False
                if min(c[0], d[0]) < a[0] < max(c[0], d[0]) and min(a[1], b[1]) < c[1] < max(a[1], b[1]):
                    return True
                return False
            elif a[1] == b[1]:  # side is horizontal
                # if c[1] == a[1] or d[1] == a[1]:  # T shape not count
                #     return False
                # if (c[1] < a[1] and d[1] < a[1]) or (c[1] > a[1] and d[1] > a[1]):  # both points of edge is on the same side
                #     return False
                if min(c[1], d[1]) < a[1] < max(c[1], d[1]) and min(a[0], b[0]) < c[0] < max(a[0], b[0]):
                    return True
                return False

        def point_is_inside(px, py):
            n = len(pos)
            j = n - 1
            cross = 0

            for i in range(n):
                xi, yi = pos[i]
                xj, yj = pos[j]

                # check if point is on the edge
                if min(xi, xj) <= px <= max(xi, xj) and min(yi, yj) <= py <= max(yi, yj):
                    return True

                # if not on the edge, count how many times cross edge to the right
                # count include edge head, exclude edge tail
                # if count is odd, point is inside
                """
                --------+   +---+
                        |   |   |   2   3
                 * ---> +---+   |1  +---+
                inside  x   x   +---+   | outside
                """
                if xi == xj and min(yi, yj) <= py < max(yi, yj) and xi > px:
                    cross += 1
                j = i
            return cross % 2 == 1

        def is_inside_the_shape(a, b):
            x1, y1 = a
            x2, y2 = b
            min_x, max_x = min(x1, x2), max(x1, x2)
            min_y, max_y = min(y1, y2), max(y1, y2)

            corners = [(x, y) for x in (min_x, max_x) for y in (min_y, max_y)]
            for px, py in corners:
                if not point_is_inside(px, py):
                    return False

            sides = [
                ((min_x, min_y), (min_x, max_y)),
                ((min_x, max_y), (max_x, max_y)),
                ((max_x, max_y), (max_x, min_y)),
                ((max_x, min_y), (min_x, min_y)),
            ]
            for side in sides:
                for edge in edges:
                    if edge_is_intersect(side, edge):
                        return False

            return True

        rects = []
        for a, b in combinations(pos, 2):
            x1, y1 = a
            x2, y2 = b

            w = abs(x1 - x2) + 1
            h = abs(y1 - y2) + 1
            area = w * h
            rects.append((area, a, b))

        rects.sort(reverse=True)

        for area, a, b in rects:
            if is_inside_the_shape(a, b):
                return area
