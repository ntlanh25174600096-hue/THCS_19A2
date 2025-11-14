tong_keo = int(input("Nhập tổng số kẹo: "))
so_hoc_sinh = int(input("Nhập số học sinh: "))
moi_hs = tong_keo // so_hoc_sinh
con_du = tong_keo % so_hoc_sinh
print(f"Mỗi học sinh nhận: {moi_hs} viên")
print(f"Số kẹo còn dư: {con_du} viên")
