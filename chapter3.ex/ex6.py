Bài 6
# 
def bubble_sort_with_count(arr):
    n = len(arr)
    swaps = 0
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swaps += 1
    return arr, swaps

data_int = [int(x) for x in input("Nhập danh sách số nguyên: ").split()]
sorted_arr, count = bubble_sort_with_count(data_int)
print(sorted_arr)
print(f"Số lần hoán đổi: {count}")
