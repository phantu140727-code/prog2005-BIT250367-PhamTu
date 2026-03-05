Bài 8
nums_list = [int(x) for x in input("Nhập danh sách số: ").split()]
found = next((x for x in nums_list if x > 10), None)
print(found)
