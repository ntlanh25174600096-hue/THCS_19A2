def kiem_tra_so_doi_xung(n):
    n_str = str(n)  
    return n_str == n_str[::-1]   
n = int(input("nhập n: "))
print(kiem_tra_so_doi_xung(n))