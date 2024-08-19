def fibonacci(n, memo={}):
    # Check if the value is already computed
    if n in memo:
        return memo[n]
    # Base cases
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        # Recursively compute Fibonacci value
        memo[n] = fibonacci(n-1, memo) + fibonacci(n-2, memo)
        return memo[n]

if __name__ == "__main__":
    print(fibonacci(159))
    # print(fibonacci(159))
