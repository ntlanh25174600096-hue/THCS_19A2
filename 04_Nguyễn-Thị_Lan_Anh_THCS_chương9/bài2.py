def giai_phuong_trinh_bac_nhat(a, b):
    if a != 0:
        x=-b/a
        print(f"phương trình có 1 nghiệm duy nhất")
    elif b != 0:
        print(f"phương trình vô nghiệm")
    else: 
        print(f"phương trình vô số nghiệm")
x = int(input("nhập a: "))
y = int(input("nhập b: "))
giai_phuong_trinh_bac_nhat(x, y)
