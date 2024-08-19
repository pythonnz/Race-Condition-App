from typing import List
import random


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            nums[i] = nums[i] * nums[i]
        return sorted(nums)


if __name__ == "__main__":
    inputs = [
        [-113, -79, -13, -1, 0, 1, 3, 10, 37, 42, 59],
        sorted([random.randint(-1000, 1000) for _ in range(36)]),
    ]

    s = Solution()
    for i in inputs:
        print(i)
        print(s.sortedSquares(i))
