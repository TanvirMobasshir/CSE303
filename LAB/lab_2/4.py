string = "Practice Problems to Drill List Comprehension in Your Head."
vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
new_string = ''

for i in string:
    if i not in vowels:
        new_string = new_string + i

print(new_string)
