d = eval(input())
r = {}

for k in d:
    if d[k] > 50:
        r[k] = d[k]

print(r)
