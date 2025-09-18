# => Strings can be stored in variables

# first_name = 'Zahid'   # this line is disabled now
# print(first_name)      # this line is also disabled

# => You can combine strings with (+)
first_name = 'Zahid'
last_name = 'Gulzar'

print(first_name + last_name)             # Output: ZahidGulzar (no space)
print('Hello ' + first_name + ' ' + last_name)  # Output: Hello Zahid Gulzar

# => You can use functions (string methods) to modify strings
sentence = 'The brown fox jumps over a lazy dog'

print(sentence.upper())        # All letters in CAPITALS
print(sentence.lower())        # All letters in lowercase
print(sentence.capitalize())   # Only the first letter of the sentence capitalized
print(sentence.count('a'))     # Count how many times 'a' appears in the sentence

# => These functions help us format strings for files, databases, or user display

# Example (disabled for now):
# first_name = input('What is your first name? : ')
# last_name = input('What is your last name? : ')
# print('Hello ' + first_name.capitalize() + ' ' + last_name.capitalize())