from heapq import merge


# For validation purposeses only.
def solution(list1, list2):
    return list(merge(list1, list2))


if __name__ == "__main__":
    print(solution([1, 1, 2, 3, 5, 8, 13, 21], [0, 2, 4, 6, 8, 10, 12]))
    print(
        solution(
            [200, 201, 204, 302, 304, 402, 404, 405, 418, 500, 501, 504],
            [202, 301, 307, 308, 400, 401, 429, 502, 503],
        )
    )
