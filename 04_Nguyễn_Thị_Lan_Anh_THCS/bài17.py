d={'a':3,'b':7,'c':5}
k=list(d.keys())[0]
for i in d:
    if d[i]>d[k]:
        k=i
print(k)