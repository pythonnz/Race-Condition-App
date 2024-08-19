def solution(n: int) -> int:
    memo = {}
    return helper(n, memo)


def helper(n: int, memo: dict[int, int]) -> int:
    if n == 0 or n == 1:
        return 1
    if n not in memo:
        memo[n] = helper(n - 1, memo) + helper(n - 2, memo)
    return memo[n]


if __name__ == "__main__":
    print(solution(32))
