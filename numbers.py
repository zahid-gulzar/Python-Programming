# => Numbers can be stored in variables
PI = 3.14159
print(PI)   # Output: 3.14159

# => You can do math with numbers
first_num = 6
second_num = 2

print(first_num + second_num)   # Addition → 8
print(first_num - second_num)   # Subtraction → 4
print(first_num / second_num)   # Division → 3.0
print(first_num * second_num)   # Multiplication → 12
print(first_num ** second_num)  # Exponentiation → 36

# => If you combine strings with numbers, Python gets confused
# days_in_feb = 28
# print(days_in_feb + ' days in February')   # ❌ TypeError

# => Convert numbers to strings before combining with other strings
days_in_feb = 28
print(str(days_in_feb) + ' days in February')   # ✅ "28 days in February"

# => Numbers can also be stored as strings
# In that case, they are treated like normal text, not numbers.
# Example (disabled):
# first_num = '5'
# second_num = '2'
# print(first_num + second_num)   # Output: "52" (string concatenation)

# => The input() function always returns strings
# Example (disabled):
# first_num = input('Enter first number: ')
# second_num = input('Enter second number: ')
# print(first_num + second_num)   # Wrong → concatenates strings

# => To do math, convert input strings into numbers
first_num = input('Enter first number: ')
second_num = input('Enter second number: ')

print(int(first_num) + int(second_num))       # Integer addition
print(float(first_num) + float(second_num))   # Float addition