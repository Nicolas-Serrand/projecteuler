
def f(n):
    return sum(i for i in range(1, n//2 + 1) if n % i == 0)

abundants = [i for i in range(1, 28124) if i < f(i)]
tab = [True for i in range(28124)]
for a in abundants:
    for b in abundants:
        if a + b < 28124:
            tab[a + b] = False

print(sum(k for k in range(28124) if tab[k]))