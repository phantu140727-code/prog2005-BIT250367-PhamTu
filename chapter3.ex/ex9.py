Bài 9
nums_list = [int(x) for x in input("Nhập danh sách số: ").split()]
odds = [x for x in nums_list if x % 2 != 0]
print(odds)
