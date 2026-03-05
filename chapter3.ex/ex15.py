text = input("Nhập chuỗi cần đảo ngược: ")

# Cách 1: Sử dụng Slicing
rev1 = text[::-1]

# Cách 2: Không sử dụng Slicing (Sử dụng vòng lặp)
rev2 = ""
for char in text:
    rev2 = char + rev2

print(f"Cách 1 (Slicing): {rev1}")
print(f"Cách 2 (Looping): {rev2}")
