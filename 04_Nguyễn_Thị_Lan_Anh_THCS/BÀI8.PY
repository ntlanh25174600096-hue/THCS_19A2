a = list(map(int, input().split()))
k = int(input())
n = len(a)
k %= n

print(a[n-k:] + a[:n-k])
