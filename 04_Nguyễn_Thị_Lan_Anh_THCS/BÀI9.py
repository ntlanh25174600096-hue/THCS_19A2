kwh = float(input("Nhập số kwh điện tiêu thụ: "))
if kwh <= 100:
    tien = kwh * 1.678
elif kwh <= 200:
    tien = kwh * 1.678 + (kwh - 100) * 1.734
else:
    tien = 100 * 1.678 + 100 * 1.734 + (kwh - 200) * 2.014
print(f"Tổng số tiền điện phải trả: {tien} VNĐ")
