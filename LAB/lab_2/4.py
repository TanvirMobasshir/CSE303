print("Student ID: 2019-2-60-025")
print("Problem 4\n")

string = "Practice Problems to Drill List Comprehension in Your Head."
vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

for vowel in vowels:
    string = string.replace(vowel, '')

print(string)
