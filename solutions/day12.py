from utils.solution_base import SolutionBase


class Solution(SolutionBase):
    def part1(self, data):
        presents = []
        while "" in data:
            idx = data.index("")
            presents.append([list(x) for x in data[1:idx]])
            data = data[idx + 1 :]
        regions = data

        def check_can_fill_all(presents, area_map, _list):
            shapes = []
            for present in presents:
                curr_shapes = set()
                for _ in range(4):
                    # rotate 90 degrees
                    present = tuple(tuple(s) for s in zip(*present[::-1]))
                    curr_shapes.add(present)
                    # flip horizontally
                    present = tuple(tuple(s[::-1]) for s in present)
                    curr_shapes.add(present)
                shapes.append(curr_shapes)

            sorted_list = sorted([idx for idx, amount in enumerate(_list) for _ in range(amount)], key=lambda idx: sum(line.count("#") for line in presents[idx]), reverse=True)

            def try_fill(present_idx, start_pos):
                if present_idx == len(sorted_list):
                    return True

                area_height, area_width = len(area_map), len(area_map[0])
                idx = sorted_list[present_idx]
                for y in range(area_height):
                    for x in range(area_width):
                        if (y, x) < start_pos:
                            continue
                        for shape in shapes[idx]:
                            h, w = len(shape), len(shape[0])
                            if y + h > area_height or x + w > area_width:
                                continue

                            valid = True
                            for dy in range(h):
                                for dx in range(w):
                                    if shape[dy][dx] == "#" and area_map[y + dy][x + dx] == "#":
                                        valid = False
                                        break
                                if not valid:
                                    break

                            if valid:
                                for dy in range(h):
                                    for dx in range(w):
                                        if shape[dy][dx] == "#":
                                            area_map[y + dy][x + dx] = "#"

                                if try_fill(present_idx + 1, (y, x)):
                                    return True

                                # failed, back to previous state
                                for dy in range(h):
                                    for dx in range(w):
                                        if shape[dy][dx] == "#":
                                            area_map[y + dy][x + dx] = "."

                return False

            return try_fill(0, (0, 0))

        count = 0
        for region in regions:
            size, _list = region.split(": ")

            x, y = map(int, size.split("x"))
            area_map = [["." for _ in range(x)] for _ in range(y)]

            _list = list(map(int, _list.split()))

            required = sum(amount * sum(row.count("#") for row in presents[idx]) for idx, amount in enumerate(_list))

            if x * y < required:
                # print(f"Region {region}: ❌ Failed. Spaces not enough.")
                continue

            valid = check_can_fill_all(presents, area_map, _list)
            if valid:
                # print(f"Region {region}: 🟢 Success.")
                count += 1
            # else:
            #     print(f"Region {region}: ❌ Failed. Cannot fit properly.")

        return count

    def part2(self, data):
        return "merry christmas"
