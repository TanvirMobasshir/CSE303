string = "Practice Problems to Drill List Comprehension in Your Head."
words = string.split()

small_word = []

for word in words:
    if len(word) < 5: small_word.append(word)

print(small_word)
