from typing import List

def solution(numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]

        prevRows = solution(numRows - 1)
        newRow = [1] * numRows

        for i in range(1, numRows - 1):
            newRow[i] = prevRows[-1][i - 1] + prevRows[-1][i]

        prevRows.append(newRow)
        return prevRows

if __name__ == "__main__":
    # print(solution(9))
    print(solution(31))
