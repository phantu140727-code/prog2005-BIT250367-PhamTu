Bài 3
colors = ["Red", "Blue", "Green", "Yellow", "Black"]
try:
    colors.remove("Green")
except ValueError:
    print("Màu Green không có trong danh sách")
print(colors)
