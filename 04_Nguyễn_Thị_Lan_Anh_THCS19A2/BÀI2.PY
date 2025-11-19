a = int(input("nhập a: "))
b = int(input("nhập b: "))
while b != 0:
    a, b = b, a % b
print("ước chung lớn nhất là:", a)