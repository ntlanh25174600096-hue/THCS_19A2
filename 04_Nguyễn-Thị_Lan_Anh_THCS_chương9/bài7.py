def la_so_hoan_hao(n):
    if n <= 1:
        return False
    tong = sum(i for i in range(1, n // 2 + 1)
                if n % i == 0)
    return tong == n

def tinh_tong_so_hoan_hao(a, b):
    return sum(so for so in range(a, b + 1) if la_so_hoan_hao(so))
a= int(input("nhập a: "))
b= int(input("nhập b: "))
tong = tinh_tong_so_hoan_hao(a, b)
print(f"Tổng số hoàn hảo trong [{a}, {b}] là: {tong}") 
