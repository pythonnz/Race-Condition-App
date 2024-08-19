from typing import List


def solution(prices: List[int]) -> int:
    buy_price = prices[0]
    profit = 0

    for p in prices[1:]:
        if buy_price > p:
            buy_price = p

        profit = max(profit, p - buy_price)

    return profit


import random


def generate_test_data(num_tests: int, value_range: tuple, size_range: tuple) -> None:
    for _ in range(num_tests):
        # size = random.randint(*size_range)  # Random size of the array
        test_data = [random.randint(*value_range) for _ in range(123)]
        return test_data
        print(test_data)


if __name__ == "__main__":
    # print(solution([1,2,10,1,10]))
    # print(solution([7,6,4,3,1]))

    # Generate 40 test data arrays with values between 1 and 10,000 and sizes between 5 and 20
    td = generate_test_data(37, (1, 1000), (5, 20))
    print(td)

    print(solution(td))
    # print(solution([19, 15, 16, 18, 9, 18, 21]))
