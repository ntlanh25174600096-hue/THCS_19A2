def kiem_tra_so_armstrong(n):
    tong = 0
    temp = n
    while temp > 0:
        chu_so = temp % 10          
        tong += chu_so ** 3        
        temp //= 10                 
    return tong == n
n = int(input("nhập n: "))
print(kiem_tra_so_armstrong(n))