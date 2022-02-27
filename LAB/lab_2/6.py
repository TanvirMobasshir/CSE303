string = "Practice Problems to Drill List Comprehension in Your Head."
words = string.split()
words_len = {}

for word in words:
    words_len[word] = len(word)

print(words_len)