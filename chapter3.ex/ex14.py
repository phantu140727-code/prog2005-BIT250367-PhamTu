def count_vowels(s):
    vowels = "aeiou"
    count = 0
    for char in s.lower():
        if char in vowels:
            count += 1
    return count

text = "Hello World"
print(f"Số lượng nguyên âm: {count_vowels(text)}")
