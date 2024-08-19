from typing import List
from collections import Counter
from random import shuffle


class Solution:
    def findJudge(self, n: int, t: List[List[int]]) -> int:
        if n == 1:
            return 1

        x = {a for a, _ in t}  # not judges
        c = Counter(b for _, b in t)  # person: num of trusters
        for a, f in c.items():
            if f == n - 1 and a not in x:
                return a

        return -1


if __name__ == "__main__":
    l1 = [
        [1, 7],
        [2, 7],
        [3, 7],
        [4, 7],
        [5, 7],
        [6, 7],
        [8, 7],
        [9, 7],
        [1, 9],
        [2, 9],
        [3, 9],
        [4, 9],
        [5, 9],
        [8, 9],
        [2, 3],
        [4, 3],
        [5, 1],
        [3, 1],
        [8, 9],
        [9, 1],
        [9, 3],
        [8, 2],
        [2, 4],
        [4, 6],
        [6, 8],
    ]
    shuffle(l1)

    l2 = [
        [1, 5],
        [2, 5],
        [4, 5],
        [5, 1],
        [1, 2],
        [2, 1],
        [3, 2],
        [4, 1],
        [4, 3],
    ]
    shuffle(l2)

    inputs = [(3, [[1, 3], [2, 3]]), (9, l1), (5, l2)]

    s = Solution()
    for i in inputs:
        print(i, ".....", s.findJudge(i[0], i[1]))
