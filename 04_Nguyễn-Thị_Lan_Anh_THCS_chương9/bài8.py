def tim_so_le_lon_nhat(a, b, c):
    so_le_list = [n for n in (a, b, c) if n % 2 != 0]
    return max(so_le_list) if so_le_list  else -1
a = int(input("nhập a:"))
b = int(input("nhập b:"))
c = int(input("nhập c:"))
print(tim_so_le_lon_nhat(a, b, c))