luong_co_ban = float(input("Nhập mức lương cơ bản: "))
so_ngay_cong = int(input("Nhập số ngày công trong tháng: "))
luong_mot_ngay = luong_co_ban / 22
tien_thuong_phat = 0
if so_ngay_cong > 22:
    tien_thuong_phat = (so_ngay_cong - 22) * luong_mot_ngay * 0.10
elif so_ngay_cong < 22:
    tien_thuong_phat = -(22 - so_ngay_cong) * luong_mot_ngay * 0.05
    tong_luong = (luong_mot_ngay * so_ngay_cong) + tien_thuong_phat

print(f"Tổng tiền lương thực nhận của nhân viên là: {tong_luong} VND")