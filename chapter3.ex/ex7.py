Bài 7
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

nums_list = [int(x) for x in input("Nhập danh sách số: ").split()]
target_num = int(input("Nhập số cần tìm: "))
print(f"Chỉ số: {linear_search(nums_list, target_num)}")
