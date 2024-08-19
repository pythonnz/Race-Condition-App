def solution(n: int) -> bool:
    print(n)
    if n == 3 or n == 1:
        return True

    if n != 0 and n % 3 == 0:
        return solution(n / 3)

    return False


if __name__ == "__main__":
    n = 3**7
    print(solution(n + 1))
