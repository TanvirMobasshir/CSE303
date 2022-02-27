string = "Practice Problems to Drill List Comprehension in Your Head."
vowels = ['a', 'e', 'i', 'o', 'u']
new_string = ''

for i in string.lower():
    if i not in vowels: new_string = new_string + i

print(new_string)
