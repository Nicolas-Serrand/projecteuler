def f(n):
    return 3*n + 1 if n % 2 else n // 2

memo = dict()
def g(n):
    if n == 1:
        return 1
    elif n in memo:
        return memo[n]
    else:
        memo[n] = 1 + g(f(n))
        return memo[n]

print(max((i for i in range(1, 1_000_000)), key=lambda j: g(j)))