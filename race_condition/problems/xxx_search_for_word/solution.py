from typing import List


def solution(board: List[List[str]], word: str) -> bool:
    m = len(board)
    n = len(board[0])

    for i in range(m):
        for j in range(n):
            if board[i][j] == word[0]:
                if dfs(board, word, 0, i, j, m, n):
                    return True
    return False


def dfs(board: List[List[str]], word: str, index: int, i: int, j: int, m: int, n: int):
    if i < 0 or i >= m or j < 0 or j >= n or board[i][j] != word[index]:
        return False
    if index == len(word) - 1:
        return True

    board[i][j] = "#"

    if (
        dfs(board, word, index + 1, i - 1, j, m, n)
        or dfs(board, word, index + 1, i + 1, j, m, n)
        or dfs(board, word, index + 1, i, j - 1, m, n)
        or dfs(board, word, index + 1, i, j + 1, m, n)
    ):
        return True

    board[i][j] = word[index]
    return False


if __name__ == "__main__":
    print(
        solution(
            board=[
                [
                    "P",
                    "A",
                    "B",
                ],
                [
                    "Y",
                    "O",
                    "N",
                ],
                [
                    "T",
                    "H",
                    "C",
                ],
            ],
            word="PYTHON",
        )
    )
    print(
        solution(
            board=[
                ["X", "E", "K", "J", "D"],
                ["F", "Q", "U", "I", "Q"],
                ["L", "E", "O", "O", "P"],
                ["M", "S", "B", "U", "H"],
                ["B", "G", "Z", "S", "C"],
            ],
            word="OBSEQUIOUS",
        )
    )
