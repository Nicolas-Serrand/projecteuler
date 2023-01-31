inputs = open("input.txt").read()

triangle = [[int(i) for i in row.split()] for row in inputs.strip().splitlines()]

n = len(triangle)
memo = {}
def f(i, j):
    if i >= n:
        return 0
    elif (i, j) not in memo:
        memo[(i, j)] = triangle[i][j] + max(f(i + 1, j),  f(i + 1, j + 1))
    return memo[(i, j)]

print(f(0, 0))