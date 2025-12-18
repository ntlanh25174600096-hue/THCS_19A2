n, m = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(n)]

p, q = map(int, input().split())
B = [list(map(int, input().split())) for _ in range(p)]

if m != p:
    print("Không nhân được")
else:
    C = [[0]*q for _ in range(n)]
    for i in range(n):
        for j in range(q):
            for k in range(m):
                C[i][j] += A[i][k] * B[k][j]
    for r in C:
        print(r)
