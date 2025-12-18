A = set(map(int, input().split()))
B = set(map(int, input().split()))

giao = []
hieu_A = []
hieu_B = []

for x in A:
    if x in B:
        giao.append(x)
    else:
        hieu_A.append(x)

for x in B:
    if x not in A:
        hieu_B.append(x)

print("A-B:", hieu_A)
print("B-A:", hieu_B)
print("A∩B:", giao)