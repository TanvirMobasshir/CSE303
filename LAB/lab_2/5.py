print("Student ID: 2019-2-60-025")
print("Problem 5\n")

string = "Practice Problems to Drill List Comprehension in Your Head."
words = string.split()
small_word = [word for word in words if len(word) < 5]
print(small_word)
