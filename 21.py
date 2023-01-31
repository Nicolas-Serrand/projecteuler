N = 10_000

def d(n):
    return sum([i for i in range(1, n//2 + 1) if n % i == 0])

k = {i:d(i) for i in range(N+1)}

ans = 0
for i in range(1, N+1):
    if k[i] in k and i == k[k[i]] and i != k[i]:
        ans += i
        
print(ans)