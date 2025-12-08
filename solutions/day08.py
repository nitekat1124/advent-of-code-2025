from utils.solution_base import SolutionBase


class Solution(SolutionBase):
    def part1(self, data):
        boxes = [list(map(int, line.split(","))) for line in data]

        pairs = {}
        for i, box1 in enumerate(boxes):
            for j, box2 in enumerate(boxes[i + 1 :], i + 1):
                # zip is slower but more readable, so I keep it here
                pairs[(i, j)] = sum((a - b) ** 2 for a, b in zip(box1, box2))

        pairs = sorted(pairs.items(), key=lambda x: x[1])

        # nums = 10 if it's test data
        nums = 10 if len(boxes) == 20 else 1000
        pairs = pairs[:nums]

        connected_sets: list[set] = []

        for (i, j), d in pairs:
            _id_i = -1
            _id_j = -1

            for idx, s in enumerate(connected_sets):
                if i in s:
                    _id_i = idx
                if j in s:
                    _id_j = idx

            match (_id_i > -1, _id_j > -1):
                case (False, False):
                    connected_sets.append(set([i, j]))
                case (True, False):
                    connected_sets[_id_i].add(j)
                case (False, True):
                    connected_sets[_id_j].add(i)
                case (True, True) if _id_i != _id_j:
                    connected_sets[_id_i] |= connected_sets[_id_j]
                    del connected_sets[_id_j]

        _lens = sorted([len(s) for s in connected_sets], reverse=True)
        return _lens[0] * _lens[1] * _lens[2]

    def part2(self, data):
        boxes = [list(map(int, line.split(","))) for line in data]

        pairs = {}
        for i, box1 in enumerate(boxes):
            for j, box2 in enumerate(boxes[i + 1 :], i + 1):
                pairs[(i, j)] = sum((a - b) ** 2 for a, b in zip(box1, box2))

        pairs = sorted(pairs.items(), key=lambda x: x[1])

        connected_sets: list[set] = []
        connected = set()

        for (i, j), d in pairs:
            connected.add(i)
            connected.add(j)

            _id_i = -1
            _id_j = -1

            for idx, s in enumerate(connected_sets):
                if i in s:
                    _id_i = idx
                if j in s:
                    _id_j = idx

            match (_id_i > -1, _id_j > -1):
                case (False, False):
                    connected_sets.append(set([i, j]))
                case (True, False):
                    connected_sets[_id_i].add(j)
                case (False, True):
                    connected_sets[_id_j].add(i)
                case (True, True) if _id_i != _id_j:
                    connected_sets[_id_i] |= connected_sets[_id_j]
                    del connected_sets[_id_j]

            if len(connected) == len(boxes) and len(connected_sets) == 1:
                return boxes[i][0] * boxes[j][0]
