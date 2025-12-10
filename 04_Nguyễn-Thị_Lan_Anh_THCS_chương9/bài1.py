def chuyen_doi_nhiet_do(do_c):
    return (do_c * 1.8) + 32
do_c = int(input("nhập độ c:"))
do_f = chuyen_doi_nhiet_do(do_c)
print(f"chuyển sang độ F là:",do_f)