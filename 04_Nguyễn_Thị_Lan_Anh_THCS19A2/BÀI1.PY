n = int(input("nhập số n: "))
i=0
while i*i < n:
     i += 1
if i*i == n:
    print(n, "là số chính phương")
else:
     print(n, "ko là số chính phương")