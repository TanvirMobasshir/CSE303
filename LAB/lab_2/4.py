string = "Practice Problems to Drill List Comprehension in Your Head."
vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

for vowel in vowels:
    string = string.replace(vowel, '')

print(string)
