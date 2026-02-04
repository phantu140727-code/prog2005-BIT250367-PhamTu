n = int(input("Nhập n: "))
if n < 2:
    print("Không phải số nguyên tố")
else:
    i = 2
    while i * i <= n:
        if n % i == 0:
            print("Không phải số nguyên tố")
            break
        i += 1
    else:
        print("Là số nguyên tố")
