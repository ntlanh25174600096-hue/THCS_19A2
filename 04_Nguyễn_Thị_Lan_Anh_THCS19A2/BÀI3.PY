tu = int(input("Tử: "))
mau = int(input("Mẫu: "))
while mau != 0:
    tu, mau = mau, tu % mau
print("Tối giản:", tu//tu, "/", mau//tu)
