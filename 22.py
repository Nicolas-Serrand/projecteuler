inputs = open("input.txt").read().strip()

names = [n.strip("\"") for n in inputs.split(",")]
names.sort()
ans = 0
for i, n in enumerate(names):
    ans += (i + 1) * sum([1 + ord(c) - ord('A') for c in n])
print(ans)