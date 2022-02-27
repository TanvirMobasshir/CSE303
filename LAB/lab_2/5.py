string = "Practice Problems to Drill List Comprehension in Your Head."
words = string.split()
small_word = [word for word in words if len(word) < 5]
print(small_word)
