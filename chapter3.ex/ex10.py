Bài 10
nums_list = [int(x) for x in input("Nhập danh sách số: ").split()]
evens = [x for x in nums_list if x % 2 == 0]
print(f"Số chẵn: {evens}")
print(f"Tổng: {sum(evens)}")
