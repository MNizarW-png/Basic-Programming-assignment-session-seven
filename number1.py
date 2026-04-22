text = "mang kasir aplikasi sederhana"

word_count = 0
char_count = 0
in_word = False

for char in text:
    if char != " ":
        char_count += 1
        if not in_word:
            word_count += 1
            in_word = True
    else:
        in_word = False

print(f"Teks: {text}")
print(f"words = {word_count}")
print(f"characters = {char_count}")
