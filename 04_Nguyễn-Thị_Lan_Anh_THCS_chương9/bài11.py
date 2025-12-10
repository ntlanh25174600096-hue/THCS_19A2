a = int(input("nhập a: "))
b = int(input("nhập b: "))
c = int(input("nhập c: "))
tinh_tich_ba_so = lambda a, b, c: a*b*c
tich = tinh_tich_ba_so(a, b, c)
print("Tích ba số là:", tich)