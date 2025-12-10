def tim_so_fibonacci(n):
    if n <= 1:          
        return n
    return tim_so_fibonacci(n - 1) + tim_so_fibonacci(n - 2)
n = int(input("nhập n: "))
print(tim_so_fibonacci(n))